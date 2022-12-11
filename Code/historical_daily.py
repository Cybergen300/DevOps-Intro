#!/usr/bin/env python3

from datetime import date 
from dateutil.relativedelta import relativedelta 
import psycopg2
from functions import get_current_price, get_historical_marketcap

#---------------------------------------------------
    #TESTING
#---------------------------------------------------

#Function inputting metrics value inside the historical_metrics table
def update_db(timestamp, price, marketcap):  
    conn= None
    try:
        conn= psycopg2.connect(
                host="localhost",
                database="ethdb",
                user="user1",
                password= "pwd"
                )
        cur = conn.cursor()  
        cur.execute("INSERT INTO historical_metrics VALUES(%s, %s, %s)", [timestamp, price, marketcap])
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

#Function making API request to API sentiment and populating the historical_metrics table inside the ethdb database
            
def populate_historical_daily():
    #Create a variable with the date from a month ago    
    timestamp = date.today()
    today = timestamp.strftime('%Y-%m-%d')
 
    ethereum_price = get_current_price('ethereum', today)
    ethereum_marketcap = get_historical_marketcap('ethereum', today, today) 

    #Extract price
    value= ethereum_price.values[0]
    value= value.astype(int)
    price= value[0]
    price = price.item()

    #Extract price
    value= ethereum_marketcap.values[0]/1000000000
    value= value.astype(int)
    marketcap= value[0]
    marketcap = marketcap.item()
    
    #Call function to populate remote ethdb 
    update_db(timestamp, price, marketcap) 


if __name__ == '__main__': 
    populate_historical_daily()
    print("Process done")

