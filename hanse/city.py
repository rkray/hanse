#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 22:36:05 2018
@author: rene@kray.info
"""

from os import listdir
import json

print("Load city Class")

"""
this function returs a list with all city objects which are defined in the
city directory on the top level
"""
def get_city_list():
    city_list=[]
    for filename in listdir("cities"):
        city=filename.split('.')[0]
        city_list.append(City(city))
    return(city_list)    

class City:
    def __init__(self,name):
        self.name=name
        print("init new HanseCity",name)
        with open('cities/'+name+'.json') as data_file:
            data = json.load(data_file)
            self.population=data['global']['population']
            self.grow_rate_per_day=data['global']['grow_rate_per_day']
            self.stock=data['stock']
            self.production=data['production']
            self.consumption=data['consumption']
            self.price_factor=data['price_factor']
            self.price={}
            self.price_update()


    """
    This function calculates the pice in dependency to the population and the
    stock in the city
    """
    def price_update(self):
        for product in self.stock.keys():
            self.price[product]=self.population/self.stock[product]*self.price_factor[product]


    """
    This function returns a string representation of a city
    """
    def __repr__(self):
        out="-- %s --\n" % self.name
        out+=" Dweller: %i\n" % self.population
        out+=" Market:\n"
        for product in self.stock:
            out+="  %6s: %6i %6.2f Gulden\n" % (
                product,
                self.stock[product],
                self.price[product]
            )
        return(out)

    """
    The following function should be used to update the city on daily base
    """
    def update(self):
        print("Update City "+self.name)
        #  Einwohnerberechung
        self.population=self.population*self.grow_rate_per_day
        #  Ereignisse (TODO)
        
        #  Rohstoffproduktion
        for product in self.production.keys():
            self.stock[product]=self.stock[product]+self.population*self.production[product]
        #  Rohstoffverbrauch
        for product in self.production.keys():
            self.stock[product]=self.stock[product]-self.population*self.consumption[product]
        #  neue Preise
        self.price_update()


if __name__ == "__main__":
    print("run city class as script")
 