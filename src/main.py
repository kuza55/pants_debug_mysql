import sqlalchemy as db

DB_NAME = "training"
DB_USER = "dolt"
DB_PASS = ""
DB_HOST = "127.0.0.1"
DB_PORT = 3306

db_string = "mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}".format(USER=DB_USER, PASSWORD=DB_PASS, HOST=DB_HOST, PORT=DB_PORT, DB_NAME=DB_NAME)

engine = db.create_engine(db_string, pool_size=20, max_overflow=20)

print(engine)