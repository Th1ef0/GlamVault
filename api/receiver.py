from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from models import Base
from sql_settings import postgresql as settings


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=True)
    return engine


engine = get_engine(
    settings["pguser"],
    settings["pgpasswd"],
    settings["pghost"],
    settings["pgport"],
    settings["pgdb"],
)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
