#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 22:12:56 2018
@author: rene@kray.info
"""

from hanse.city import get_city_list

print("Start Hanse Game")

cities=get_city_list()

for city in cities:
    print(city)