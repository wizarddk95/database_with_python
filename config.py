import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()

if __name__ == "__main__":
    print(settings.DATABASE_URL)