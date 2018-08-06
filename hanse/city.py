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
this function returs a list with all city objects which are defind in the
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
            self.consumtion=data['consumtion']

    """
    This function returns a string representation of a city
    """
    def __repr__(self):
        out="-- %s --\n" % self.name
        out+=" Dweller: %i\n" % self.population
        out+=" Market:\n"
        for product in self.stock:
            out+="  %10s: %10i\n" % (product,self.stock[product])
        
        
        return(out)

    def update(self):
        print "Update CIty "+self.name
        # ToDo
        #  Einwohnerberechung
        #  Ereignisse
        #  Rohstoffproduktion
        #  Rohstoffverbrauch
        #  neue Preise

if __name__ == "__main__":
    print("run city class as script")
 