#!/usr/bin/env python3

from datetime import date 
from dateutil.relativedelta import relativedelta 
import psycopg2
from functions import get_historical_price, get_historical_marketcap


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
            
def populate_table():
    #Create a variable with the current date     
    today = date.today()
    today = today.strftime('%Y-%m-%d')
    type(today)  
 
    #Create a variable with the date from 6 months ago    
    six_months = date.today() + relativedelta(months=-6)
    six_months = six_months.strftime('%Y-%m-%d')
    type(six_months)

    ethereum_price = get_historical_price('ethereum', six_months, today)
    ethereum_marketcap = get_historical_marketcap('ethereum', six_months, today) 
    
    counter= len(ethereum_price)
    
    for i in range(0, counter):
        
        #extract date
        timestamp = ethereum_price.index[i]  
        
        #extract historical price
        value= ethereum_price.values[i]
        value= value.astype(int)
        price= value[0]
        price = price.item()
        
        #extract historical marketcap in billions of $
        value= ethereum_marketcap.values[i]/1000000000
        value= value.astype(int)
        marketcap= value[0]
        marketcap = marketcap.item()
        #Call function to populate remote ethdb 

        update_db(timestamp, price, marketcap) 


if __name__ == '__main__': 
    populate_table()
    print("Process done")
