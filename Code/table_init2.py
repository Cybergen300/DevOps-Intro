#!/usr/bin/env python3

from datetime import date 
from dateutil.relativedelta import relativedelta 
import psycopg2
from functions import get_current_price, get_current_volume, get_daily_active_address

#Function inputting metrics value inside the historical_metrics table
def update_db(timestamp, price, volume, address):  
    conn= None
    try:
        conn= psycopg2.connect(
                host="localhost",
                database="ethdb",
                user="user1",
                password= "pwd"
                )
        cur = conn.cursor()  
        cur.execute("INSERT INTO daily_metrics VALUES(%s, %s, %s, %s)", [timestamp, price, volume, address])
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

#Function making API request to API sentiment and populating the historical_metrics table inside the ethdb database
            
def populate_table_daily():
 
    #Create a variable with the date of today    
    timestamp = date.today()
    today = timestamp.strftime('%Y-%m-%d')

    #Santiment API calls 
    ethereum_current_price = get_current_price('ethereum', today) 
    ethereum_current_volume = get_current_volume('ethereum', today) 
    ethereum_daily_active_address = get_daily_active_address('ethereum', today)

    #Extract price
    value= ethereum_current_price.values[0]
    value= value.astype(int)
    price= value[0]
    price = price.item()
    
    #Extract volume in billions
    value= ethereum_current_volume.values[0]/1000000000
    value= value.astype(int)
    volume= value[0]
    volume = volume.item()
    
    #Extract 24h active addresses
    value= ethereum_daily_active_address.values[0]
    value= value.astype(int)
    activeAddress= value[0]
    activeAddress = activeAddress.item()

    #Call function to populate remote ethdb 
    update_db(timestamp, price, volume, activeAddress) 


if __name__ == '__main__': 
    populate_table_daily()
    print("Process done") 

