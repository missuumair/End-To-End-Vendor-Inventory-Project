import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",       # log file path
    filemode="a",             # 'w' to overwrite, 'a' to append
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")

engine = create_engine("mysql+pymysql://root:Mohammed313@localhost:3306/inventory")

def ingest_db(df,table_name, engine):
    ''' This Function will Ingest The Data To MYSQL Date Base Tables'''
    df.to_sql(table_name, con = engine , if_exists = 'replace' , index = False)

def load_raw_data():
    '''This Function Loads the CSVs from the Date to mysal inventory DB'''
    start = time.time()
    for File in os.listdir('Data'):
        if '.csv' in File:
            df = pd.read_csv('Data/'+File)
            print(df.shape)
            ingest_db(df ,File[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('----------Ingest Completed-----------')
    
    logging.info(f"\nTotal Time Taken : {total_time} minutes")

if __name__ == "__main__":
    load_raw_data()