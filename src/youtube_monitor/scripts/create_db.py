from youtube_monitor.database import Base, engine

def create_database():
  Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Creating database tables...")
    create_database()
    print("Database tables created.")
