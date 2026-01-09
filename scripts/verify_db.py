import asyncio
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.englishhub_bot.database.engine import init_db
from src.englishhub_bot.config import settings

async def main():
    print(f"Database URL: {settings.DATABASE_URL}")
    print("Creating tables...")
    try:
        await init_db()
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")
        exit(1)

if __name__ == "__main__":
    asyncio.run(main())
