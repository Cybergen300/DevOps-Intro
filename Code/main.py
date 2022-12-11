#!/usr/bin/env python3

from network_growth import populate_network_growth 
from historical_daily import populate_historical_daily 
from table_init2  import populate_table_daily 
from table_init3 import populate_table_delayed 


if __name__ == '__main__': 
    populate_network_growth()
    populate_historical_daily()    
    populate_table_daily()
    populate_table_delayed()
    print("Process done")  