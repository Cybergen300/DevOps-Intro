#!/usr/bin/env python3

from datetime import date 
from dateutil.relativedelta import relativedelta 
import psycopg2
from functions import get_daily_circulation, get_daily_velocity, get_daily_social_volume, get_top_holders, get_current_dev_activity, get_current_github_acti>


#Function inputting metrics value inside the historical_metrics table
def update_db(timestamp, circulation, velocity, socialVol, topHolders, devActivity, githubActivity):  
    conn= None
    try:
        conn= psycopg2.connect(
                host="localhost",
                database="ethdb",
                user="user1",
                password= "pwd"
                )
        cur = conn.cursor()  
        cur.execute("INSERT INTO delayed_metrics VALUES(%s, %s, %s, %s, %s, %s, %s)", [timestamp, circulation, velocity, socialVol, topHolders, devActivity,>
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

#Function making API request to API sentiment and populating the historical_metrics table inside the ethdb database
            
def populate_table_delayed():
 
    #Create a variable with the date from a month ago
    timestamp = date.today() + relativedelta(months=-1)
    last_month = timestamp.strftime('%Y-%m-%d')
  

    #Santiment API calls 
    ethereum_daily_circulation = get_daily_circulation('ethereum', last_month)
    ethereum_daily_velocity = get_daily_velocity('ethereum', last_month)
    ethereum_daily_social_volume = get_daily_social_volume('ethereum', last_month)  
    ethereum_top_holder = get_top_holders('ethereum', last_month)   
    ethereum_current_dev_activity = get_current_dev_activity('ethereum', last_month)    
    ethereum_current_github_activity = get_current_github_activity('ethereum', last_month) 

    #Extract circulation
    value= ethereum_daily_circulation.values[0]
    value= value.astype(int)
    circulation= value[0]
    circulation = circulation.item()
    
    #Extract velocity
    value= ethereum_daily_velocity.values[0]
    value= value.astype(int)
    velocity= value[0]
    velocity = velocity.item()
    
    #Extract social volume
    value= ethereum_daily_social_volume.values[0]
    value= value.astype(int)
    socialVol= value[0]
    socialVol = socialVol.item()

    #Extract top Holders holding
    value= ethereum_top_holder.values[0]
    value= value.astype(int)
    topHolders= value[0]
    topHolders = topHolders.item()

    #Extract development activity
    value= ethereum_current_dev_activity.values[0]
    value= value.astype(int)
    devActivity= value[0]
    devActivity = devActivity.item()

    #Extract github activity
    value= ethereum_current_github_activity.values[0]
    value= value.astype(int)
    githubActivity= value[0]
    githubActivity = githubActivity.item()

    #Call function to populate remote ethdb 
    update_db(timestamp, circulation, velocity, socialVol, topHolders, devActivity, githubActivity) 


if __name__ == '__main__': 
    populate_table_delayed()
    print("Process done")      


