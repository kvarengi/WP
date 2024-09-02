import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.database import models
from sqlalchemy import select


TEST_DB = "tmp/test_db.sqlite3.db"


class TestDBMethods(unittest.TestCase):
    engine = create_engine(f"sqlite:///{TEST_DB}")

    def test_insertion_and_selection(self):
        models.Base.metadata.create_all(self.engine)

        with Session(self.engine) as session:
            user = models.User(
                tg_user_id=12345,
                matter_ballance=0.234,
                idea_ballance=2.412,
                tg_wallet_or_metamask_address="nu adress",
                created_at=17253067532,
            )
            bet = models.Bet(
                user_id=0,
                block_id=0,
                bet_percent=0.1,
                start_matter_price=1.1,
                start_idea_price=1.2,
                start_at=1725305842,
                end_at=17253067588,
            )
            block = models.Block(
                state=0, prev_block_hash="aboba", created_at="17253067500"
            )
            session.add_all([user, bet, block])
            print(f"INSERTED USER: {user}")
            print(f"INSERTED BET: {bet}")
            print(f"INSERTED BLOCK: {block}")
            session.commit()

        with Session(self.engine) as session:
            stmt = select(models.User).where(models.User.id == 1)
            for user in session.scalars(stmt):
                print(f"SELECTED USER: {user}")
            stmt = select(models.Bet).where(models.Bet.id == 1)
            for bet in session.scalars(stmt):
                print(f"SELECTED BET: {bet}")
            stmt = select(models.Block).where(models.Block.id == 1)
            for block in session.scalars(stmt):
                print(f"SELECTED BLOCK: {block}")


if __name__ == "__main__":
    open(TEST_DB, "w").close()
    unittest.main()
