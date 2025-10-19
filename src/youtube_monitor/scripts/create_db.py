from youtube_monitor.youtube_monitor.database import Base, engine

def create_database():
  Base.metadata.create_all(bind=engine)

if name == "__main__":
    print("Creating database tables...")
    create_database()
    print("Database tables created.")
