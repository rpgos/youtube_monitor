from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from youtube_monitor.youtube_checker import check_channels
from youtube_monitor.config import Config

config = Config()

app = FastAPI(title="YouTube Monitor")

scheduler = BackgroundScheduler()
scheduler.add_job(check_channels, "interval", minutes=config.check_interval)
scheduler.start()

@app.on_event("startup")
async def startup_event():
    check_channels()  # run once on startup

@app.get("/")
async def root():
    return {"status": "running", "check_interval": config.check_interval}

# if __name__ == "__main__":
