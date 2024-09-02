from sqlalchemy import Boolean, Float, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    tg_user_id: Mapped[int]
    matter_ballance: Mapped[float] = mapped_column(Float(precision=64))
    idea_ballance: Mapped[float] = mapped_column(Float(precision=64))
    # 42 for Metamask and 48 for TON wallet  TODO : Check more attentively
    tg_wallet_or_metamask_address: Mapped[str] = mapped_column(String(48))
    created_at: Mapped[int]  # UNIX timestamp

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, is_admin={self.is_admin!r}, tg_user_id={self.tg_user_id!r}, matter_ballance={self.matter_ballance}, idea_ballance={self.idea_ballance}, tg_wallet_or_metamask_address={self.tg_wallet_or_metamask_address}, created_at={self.created_at})"


class Bet(Base):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    block_id: Mapped[int] = mapped_column(ForeignKey("blocks.id"))
    bet_percent: Mapped[float] = mapped_column(Float(precision=64))
    start_matter_price: Mapped[float] = mapped_column(Float(precision=64))
    start_idea_price: Mapped[float] = mapped_column(Float(precision=64))
    start_at: Mapped[int]  # UNIX timestamp
    end_at: Mapped[int]  # UNIX timestamp

    def __repr__(self) -> str:
        return f"Bet(id={self.id}, user_id={self.user_id}, block_id={self.block_id}, bet_percent={self.bet_percent}, start_matter_price={self.start_matter_price}, start_idea_price={self.start_idea_price}, start_at={self.start_at}, end_at={self.end_at})"


class Block(Base):
    __tablename__ = "blocks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    state: Mapped[int]  # HZ cho eto
    prev_block_hash: Mapped[str]  # = mapped_column(String( TODO : add max hash length))
    created_at: Mapped[int]  # UNIX timestamp

    def __repr__(self) -> str:
        return f"Block(id={self.id}, state={self.state}, prev_block_hash={self.prev_block_hash}, created_at={self.created_at})"
