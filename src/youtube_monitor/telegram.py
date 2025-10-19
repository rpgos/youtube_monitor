import requests
from youtube_monitor.config import Config

config = Config()

def send_message(text: str):
    url = f"https://api.telegram.org/bot{confif.telegram_bot_token}/sendMessage"
    data = {
        "chat_id": config.telegram_chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False,
    }
    requests.post(url, data=data)
