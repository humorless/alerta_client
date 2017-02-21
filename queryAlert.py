#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import json

"""
pagniation: Use limit to restrict how many items can stay in one page. 
            Use page to choose which page.

"""

apiKey = 'nskKwHlzEIuTejKqcYKT7-IB_owdw7Dd8sGhXceA'
headers={'Authorization':'Key '+ apiKey}

url = "http://10.20.30.40:8181/api/alerts"
payload = {"limit":5,
           "status":"open",
           "page":77,
           "origin":"NQM"}
r = requests.get(url, params=payload, headers=headers)
print r.text


print " ============================ "

"""
search options:
alert attributes such as origin can be set as query parameters.
http://alerta.readthedocs.io/en/latest/api/reference.html#search-alerts
http://explorer.alerta.io/#/query
"""

payload = {"limit":1000,
           "status":"open",
           "origin":"owl"}

r = requests.get(url, params=payload, headers=headers)
print r.text
