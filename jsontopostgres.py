import asyncio
import json
from datetime import datetime

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import PremiumUsers
from database import async_session


def date_to_timestamp(date_str: str) -> int:
    # format: DD.MM.YYYY
    dt = datetime.strptime(date_str, "%d.%m.%Y")
    return int(dt.timestamp())


def load_premium_from_json(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    # premium jadvalini topamiz
    table = next(
        item for item in raw
        if item.get("type") == "table" and item.get("name") == "premium"
    )

    return table["data"]


async def import_premium_users(json_path: str):
    rows = load_premium_from_json(json_path)

    values = []
    for row in rows:
        values.append({
            "chat_id": int(row["chat_id"]),
            "start_at": date_to_timestamp(row["start"]),
            "end_at": date_to_timestamp(row["end"]),
            "file_id": row.get("rasm")  # xohlasangiz
        })

    async with async_session() as session:  # type: AsyncSession
        stmt = insert(PremiumUsers).values(values)
        await session.execute(stmt)
        await session.commit()


asyncio.run(
    import_premium_users("premium.json")
)
