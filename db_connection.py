import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

def db_creation(DataFrame, name):
	pgconn =  psycopg2.connect(
		database = "initial_db",
		host = 'wb-data.cbosee62k42d.eu-north-1.rds.amazonaws.com',
		user = "postgres",
		port = 5432,
		password = "padington"
	)

	pgcursor = pgconn.cursor()
	engine = create_engine('postgresql+psycopg2://postgres:padington@wb-data.cbosee62k42d.eu-north-1.rds.amazonaws.com:5432/initial_db')
	DataFrame.to_sql(name, engine, if_exists = 'append', index = False)
	pgconn.close()