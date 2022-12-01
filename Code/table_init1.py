#!/usr/bin/env python3

from datetime import date 
from dateutil.relativedelta import relativedelta 
import psycopg2
from functions import get_current_network_growth

def update_db(timestamp, growth):  
    conn= None
    try:
        conn= psycopg2.connect(
                host="localhost",
                database="ethdb",
                user="user1",
                password= "pwd"
                )
        cur = conn.cursor()  
        cur.execute("INSERT INTO network_growth VALUES(%s, %s)", [timestamp, growth])
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

#Function making API request to API sentiment and populating the historical_metrics table inside the ethdb database
            
def populate_table():
 
    #Create a variable with the date from a month ago    
    last_month = date.today() + relativedelta(months=-1)
    last_month = last_month.strftime('%Y-%m-%d')
    type(last_month)  
    
    six_months = date.today() + relativedelta(months=-6)
    six_months = six_months.strftime('%Y-%m-%d')
    type(six_months)

    ethereum_network_growth = get_current_network_growth('ethereum', six_months, last_month) 

    
    counter= len(ethereum_network_growth)
    
    for i in range(0, counter):
        
        #extract date
        timestamp = ethereum_network_growth.index[i]
        
        
        #extract historical network growth
        value= ethereum_network_growth.values[i]
        value= value.astype(int)
        growth= value[0]
        growth = growth.item()

        #Call function to populate remote ethdb 
        update_db(timestamp, growth) 


if __name__ == '__main__': 
    populate_table()
    print("Process done")

