
from sqlalchemy import create_engine, BigInteger, Column, DateTime, Time, String, Integer, Enum, DECIMAL, TIMESTAMP, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.base import Base

class UK_lotto(Base):
    __tablename__ = 'UK_lotto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    draw_number = Column(BigInteger, primary_key=True)
    draw_date = Column(Date, primary_key=True)
    draw_time = Column(Time, nullable=False, default='00:00:00')
    draw_column = Column(String(200), nullable=False )
    joker = Column(String(50), nullable=False, default='' )
    balander = Column(String(50), nullable=False, default='' )
    columns = Column(BigInteger, nullable=True, default=0)
    total_winners = Column(BigInteger, nullable=False, default=0)
    win_nums_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    all_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    FR_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    dividents_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    winners = Column(String(500) )
    FR_winners = Column(String(500) )
    dividents = Column(String(500) )
    jackpots = Column(String(500) )
    millionaire_maker = Column(String(500) )
    next_jackpot_1 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    next_jackpot_2 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    win_ratio = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    outcome = Column(String(100) )

    multi_winners = Column(String(500), nullable=True)
    multiplier = Column(Integer, nullable=True)
    big_winners_5M = Column(String(500), nullable=True)
    big_winners_5 = Column(String(500), nullable=True)

    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = {
        'mysql_collate': 'utf8_unicode_ci'
    }


class UK_lotto_hotpicks(Base):
    __tablename__ = 'UK_lotto_hotpicks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    draw_number = Column(BigInteger, primary_key=True)
    draw_date = Column(Date, primary_key=True)
    draw_time = Column(Time, nullable=False, default='00:00:00')
    draw_column = Column(String(200), nullable=False )
    joker = Column(String(50), nullable=False, default='' )
    balander = Column(String(50), nullable=False, default='' )
    columns = Column(BigInteger, nullable=True, default=0)
    total_winners = Column(BigInteger, nullable=False, default=0)
    win_nums_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    all_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    FR_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    dividents_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    winners = Column(String(500) )
    FR_winners = Column(String(500) )
    dividents = Column(String(500) )
    jackpots = Column(String(500) )
    millionaire_maker = Column(String(500) )
    next_jackpot_1 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    next_jackpot_2 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    win_ratio = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    outcome = Column(String(100) )

    multi_winners = Column(String(500), nullable=True)
    multiplier = Column(Integer, nullable=True)
    big_winners_5M = Column(String(500), nullable=True)
    big_winners_5 = Column(String(500), nullable=True)

    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = {
        'mysql_collate': 'utf8_unicode_ci'
    }


class UK_euromillions(Base):
    __tablename__ = 'UK_euromillions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    draw_number = Column(BigInteger, primary_key=True)
    draw_date = Column(Date, primary_key=True)
    draw_time = Column(Time, nullable=False, default='00:00:00')
    draw_column = Column(String(200), nullable=False )
    joker = Column(String(50), nullable=False, default='' )
    balander = Column(String(50), nullable=False, default='' )
    columns = Column(BigInteger, nullable=True, default=0)
    total_winners = Column(BigInteger, nullable=False, default=0)
    win_nums_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    all_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    FR_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    dividents_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    winners = Column(String(500) )
    FR_winners = Column(String(500) )
    dividents = Column(String(500) )
    jackpots = Column(String(500) )
    millionaire_maker = Column(String(500) )
    next_jackpot_1 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    next_jackpot_2 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    win_ratio = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    outcome = Column(String(100) )

    multi_winners = Column(String(500), nullable=True)
    multiplier = Column(Integer, nullable=True)
    big_winners_5M = Column(String(500), nullable=True)
    big_winners_5 = Column(String(500), nullable=True)

    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = {
        'mysql_collate': 'utf8_unicode_ci'
    }


class UK_euromillions_hotpicks(Base):
    __tablename__ = 'UK_euromillions_hotpicks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    draw_number = Column(BigInteger, primary_key=True)
    draw_date = Column(Date, primary_key=True)
    draw_time = Column(Time, nullable=False, default='00:00:00')
    draw_column = Column(String(200), nullable=False )
    joker = Column(String(50), nullable=False, default='' )
    balander = Column(String(50), nullable=False, default='' )
    columns = Column(BigInteger, nullable=True, default=0)
    total_winners = Column(BigInteger, nullable=False, default=0)
    win_nums_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    all_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    FR_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    dividents_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    winners = Column(String(500) )
    FR_winners = Column(String(500) )
    dividents = Column(String(500) )
    jackpots = Column(String(500) )
    millionaire_maker = Column(String(500) )
    next_jackpot_1 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    next_jackpot_2 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    win_ratio = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    outcome = Column(String(100) )

    multi_winners = Column(String(500), nullable=True)
    multiplier = Column(Integer, nullable=True)
    big_winners_5M = Column(String(500), nullable=True)
    big_winners_5 = Column(String(500), nullable=True)

    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = {
        'mysql_collate': 'utf8_unicode_ci'
    }


class UK_thunderball(Base):
    __tablename__ = 'UK_thunderball'

    id = Column(Integer, primary_key=True, autoincrement=True)
    draw_number = Column(BigInteger, primary_key=True)
    draw_date = Column(Date, primary_key=True)
    draw_time = Column(Time, nullable=False, default='00:00:00')
    draw_column = Column(String(200), nullable=False )
    joker = Column(String(50), nullable=False, default='' )
    balander = Column(String(50), nullable=False, default='' )
    columns = Column(BigInteger, nullable=True, default=0)
    total_winners = Column(BigInteger, nullable=False, default=0)
    win_nums_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    all_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    FR_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    dividents_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    winners = Column(String(500) )
    FR_winners = Column(String(500) )
    dividents = Column(String(500) )
    jackpots = Column(String(500) )
    millionaire_maker = Column(String(500) )
    next_jackpot_1 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    next_jackpot_2 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    win_ratio = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    outcome = Column(String(100) )

    multi_winners = Column(String(500), nullable=True)
    multiplier = Column(Integer, nullable=True)
    big_winners_5M = Column(String(500), nullable=True)
    big_winners_5 = Column(String(500), nullable=True)

    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = {
        'mysql_collate': 'utf8_unicode_ci'
    }


class UK_set_for_life(Base):
    __tablename__ = 'UK_set_for_life'

    id = Column(Integer, primary_key=True, autoincrement=True)
    draw_number = Column(BigInteger, primary_key=True)
    draw_date = Column(Date, primary_key=True)
    draw_time = Column(Time, nullable=False, default='00:00:00')
    draw_column = Column(String(200), nullable=False )
    joker = Column(String(50), nullable=False, default='' )
    balander = Column(String(50), nullable=False, default='' )
    columns = Column(BigInteger, nullable=True, default=0)
    total_winners = Column(BigInteger, nullable=False, default=0)
    win_nums_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    all_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    FR_winners_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    dividents_flag = Column(Enum('Y', 'N' ), nullable=False, default='Y')
    winners = Column(String(500) )
    FR_winners = Column(String(500) )
    dividents = Column(String(500) )
    jackpots = Column(String(500) )
    millionaire_maker = Column(String(500) )
    next_jackpot_1 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    next_jackpot_2 = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    win_ratio = Column(DECIMAL(20, 2), nullable=False, default=0.00)
    outcome = Column(String(100) )

    multi_winners = Column(String(500), nullable=True)
    multiplier = Column(Integer, nullable=True)
    big_winners_5M = Column(String(500), nullable=True)
    big_winners_5 = Column(String(500), nullable=True)

    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = {
        'mysql_collate': 'utf8_unicode_ci'
    }
