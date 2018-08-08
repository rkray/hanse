#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 22:12:56 2018
@author: rene@kray.info
"""
from datetime import date, timedelta
from hanse.city import get_city_list

print("╔══════════════════╗")
print("║ Start Hanse Game ║")
print("╚══════════════════╝")

today=date(1500,1,1)

cities=get_city_list()

# MAINLOOP
#  City update
#  Ship update
#  User-Interface

def menu():
    out= "┌──────────────┬───────────┬─────────────┐\n"
    out+="│ Next Day (n) │ Trade (t) │ Give Up (q) │\n"
    out+="└──────────────┴───────────┴─────────────┘"
    return(out)

while True: 
    for city in cities:
        print(city)
    print(menu())
    user_input = input("[%s] What do you want to do today?"%(str(today)))
    if user_input=="n":
        for city in cities:
            city.update()
        print("Next Day")
        today=today+timedelta(days=1)
        
    elif user_input=="t":
        #go to trade interface
        print("Trade")
    elif user_input=="q":
        print("Bye Bye")
        exit()
