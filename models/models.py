from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    file_id: Mapped[str | None] = mapped_column(String(255), nullable=True)

class PremiumUsers(Base):
    __tablename__ = "premium_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    file_id: Mapped[str | None] = mapped_column(String(255), nullable=True)

    start_at: Mapped[int] = mapped_column(BigInteger, nullable=False)
    end_at: Mapped[int] = mapped_column(BigInteger, nullable=False)

class BotSleep(Base):
    __tablename__ = "bot_sleep"

    id: Mapped[int] = mapped_column(primary_key=True)
    sleep_time: Mapped[int] = mapped_column(BigInteger, nullable=False)

class BanUsers(Base):
    __tablename__ = "ban_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    ban_time: Mapped[int] = mapped_column(BigInteger, nullable=False)