import os
import glob
import asyncio
from datetime import datetime
from aiogram import Bot
from config import ADMINS

DB_NAME = "premiumbot"
DB_USER = "postgres"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)

BACKUP_INTERVAL = 60 * 60 * 24  # 24 soat

async def backup_and_send(bot):
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = f"{BACKUP_DIR}/db_backup_{today}.sql"

    # 🗑 eski backupni o‘chirish
    for old in glob.glob(f"{BACKUP_DIR}/db_backup_*.sql"):
        os.remove(old)

    # 📦 backup olish
    os.system(f"PGPASSWORD='123' pg_dump -U {DB_USER} {DB_NAME} > {file_path}")

    # 📤 yuborish
    with open(file_path, "rb") as f:
        await bot.send_document(ADMINS[0], f)


async def scheduler(bot: Bot):
    while True:
        try:
            await backup_and_send(bot)
        except Exception as e:
            await bot.send_message(ADMINS[0], f"❗ Backup xato: {e}")

        await asyncio.sleep(BACKUP_INTERVAL)
