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
def populate_network_growth():
 
    #Create a variable with the date from a month ago
    timestamp = date.today() + relativedelta(months=-1)
    last_month = timestamp.strftime('%Y-%m-%d')

    #Create a variable with the date from a month ago    
    last_month = date.today() + relativedelta(months=-1)
    last_month = last_month.strftime('%Y-%m-%d')
    type(last_month)  
    
    ethereum_network_growth = get_current_network_growth('ethereum', last_month, last_month)

    #Extract network growth 
    value= ethereum_network_growth.values[0]
    value= value.astype(int)
    networkGrowth= value[0]
    networkGrowth = networkGrowth.item()    

    #Call function to populate remote ethdb 
    update_db(timestamp, networkGrowth) 

if __name__ == '__main__': 
    populate_network_growth()
    print("Process done")
