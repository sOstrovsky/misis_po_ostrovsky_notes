import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from os import environ
from dotenv import load_dotenv

load_dotenv()

db_user = environ.get('PGUSER')
db_password = environ.get('POSTGRES_PASSWORD')
db_host = environ.get('DB_HOST')
db_name = environ.get('POSTGRES_DB')

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()

if not _sql.inspect(engine).has_table("notes"):
    Base.metadata.create_all(bind=engine)
