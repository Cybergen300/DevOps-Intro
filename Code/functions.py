#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:14:50 2022

@author: goudurix
"""
import san
from datetime import date 
from dateutil.relativedelta import relativedelta 


#-----------------------------------------------
#Functions to extract metrics from Santiment API
#-----------------------------------------------


#Function to extract historical prices 
#Notes: All functions inputs should be str

def get_historical_price(asset, start_date, end_date): 
    historical_price= san.get(
            "price_usd", 
            slug= asset, 
            from_date= start_date,
            to_date= end_date,
            interval="1d"
    )   
    return historical_price


#Function to extract historical marketcap 
#Notes: All functions inputs should be str

def get_historical_marketcap(asset, start_date, end_date): 
    historical_marketcap= san.get(
            "marketcap_usd", 
            slug= asset, 
            from_date= start_date,
            to_date= end_date,
            interval="1d"
    )   
    return historical_marketcap


#Function to extract current asset price 
#Notes: All functions inputs should be str

def get_current_price(asset, date): 
    current_price= san.get(
            "price_usd", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_price


#Function to extract current volume in USD 
#Notes: All functions inputs should be str

def get_current_volume(asset, date): 
    current_volume= san.get(
            "volume_usd", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_volume

#Function to extract current number of Ethereum active address 
#Notes: All functions inputs should be str
def get_daily_active_address(asset, date): 
    current_active_address= san.get(
            "active_addresses_24h", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_active_address

#Function to extract current daily token circulation
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan 
    
def get_daily_circulation(asset, date): 
    current_circulation= san.get(
            "circulation_1d", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_circulation

#Function to extract current daily token velocity
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan 
def get_daily_velocity(asset, date): 
    current_velocity= san.get(
            "velocity", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_velocity


#Function to extract current daily network social volume
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan 
def get_daily_social_volume(asset, date): 
    current_social_volume= san.get(
            "social_volume_total", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_social_volume


#Function to extract current top 10 holders holdings
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan 
def get_top_holders(asset, date): 
    top_holder= san.get(
            "amount_in_top_holders", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return top_holder



#Function to extract current dev activity
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan 
def get_current_dev_activity(asset, date): 
    current_dev_activity= san.get(
            "dev_activity", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_dev_activity


#Function to extract current github activity
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan
def get_current_github_activity(asset, date): 
    current_github_activity= san.get(
            "github_activity", 
            slug= asset, 
            from_date= date,
            to_date= date,
            interval="1d"
    )   
    return current_github_activity


#Function to extract current network growth
#Notes: All functions inputs should be str
#Last month value due to limitation of free plan
def get_current_network_growth(asset, start_date, end_date): 
    current_network_growth= san.get(
            "network_growth", 
            slug= asset, 
            from_date= start_date,
            to_date= end_date,
            interval="1d"
    )   
    return current_network_growth





#---------------------------------------------------
    #TESTING
#---------------------------------------------------

if __name__ == "__main__":
    
    today = date.today()
    today = today.strftime('%Y-%m-%d')
    type(today)
    
    last_month = date.today() + relativedelta(months=-1)
    last_month = last_month.strftime('%Y-%m-%d')
    type(last_month)    
    
    six_months = date.today() + relativedelta(months=-6)
    six_months = six_months.strftime('%Y-%m-%d')
    type(six_months)

    
    #test 
    ethereum_price = get_historical_price('ethereum', six_months, today)
    ethereum_marketcap = get_historical_marketcap('ethereum', six_months, today) 
    ethereum_current_price = get_current_price('ethereum', today) 
    ethereum_current_volume = get_current_volume('ethereum', today) 
    ethereum_daily_active_address = get_daily_active_address('ethereum', today)
    ethereum_daily_circulation = get_daily_circulation('ethereum', last_month)
    ethereum_daily_velocity = get_daily_velocity('ethereum', last_month)
    ethereum_daily_social_volume = get_daily_social_volume('ethereum', last_month)  
    ethereum_top_holder = get_top_holders('ethereum', last_month)   
    ethereum_current_dev_activity = get_current_dev_activity('ethereum', last_month)    
    ethereum_current_github_activity = get_current_github_activity('ethereum', last_month)   
    ethereum_network_growth = get_current_network_growth('ethereum', six_months, last_month)   
    