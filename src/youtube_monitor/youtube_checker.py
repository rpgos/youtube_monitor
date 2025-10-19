import requests
from datetime import datetime
from youtube_monitor.config import Config
from youtube_monitor.database import SessionLocal
from youtube_monitor.models import Video
from youtube_monitor.telegram import send_message

# Example channel list
CHANNELS = {
    "Linus Tech Tips": "UCXuqSBlHAE6Xw-yeJA0Tunw",
    "Marques Brownlee": "UCBJycsmduvYEL83R_U4JriQ",
}

config = Config()

def get_latest_video(channel_id: str):
    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?key={config.youtube_api_key}&channelId={channel_id}"
        f"&part=snippet,id&order=date&maxResults=1"
    )
    resp = requests.get(url).json()
    items = resp.get("items", [])
    if not items:
        return None
    item = items[0]
    return {
        "videoId": item["id"]["videoId"],
        "title": item["snippet"]["title"],
        "publishedAt": item["snippet"]["publishedAt"],
    }


def check_channels():
    db = SessionLocal()
    new_videos = []

    for name, channel_id in CHANNELS.items():
        latest = get_latest_video(channel_id)
        if not latest:
            continue

        existing = db.query(Video).filter(Video.video_id == latest["videoId"]).first()
        if existing:
            continue  # Already seen

        # New video found
        vid = Video(
            video_id=latest["videoId"],
            channel_id=channel_id,
            title=latest["title"],
            published_at=datetime.fromisoformat(latest["publishedAt"].replace("Z", "+00:00")),
        )
        db.add(vid)
        db.commit()
        new_videos.append((name, vid))

    db.close()

    if new_videos:
        message = "📢 *New YouTube Uploads:*\n\n"
        for name, vid in new_videos:
            link = f"https://www.youtube.com/watch?v={vid.video_id}"
            message += f"• {name}: [{vid.title}]({link})\n"
        send_message(message)
