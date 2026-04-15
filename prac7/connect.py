import psycopg2
from config import load_config


def connect():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            print("Connected to the PostgreSQL server.")

            return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None