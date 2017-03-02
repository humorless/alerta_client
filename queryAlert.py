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

url = "http://alert.owl.fastweb.com.cn/api/alerts?from-date=2017-02-24T00:00:00.000Z"
#url = "http://10.20.30.40:8181/api/alerts"
payload = {"limit":20,
           "status":"open",
           "page":1,
           "origin":"NQM",
           "sort-by":"attributes.ping",
           "reverse": True}
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
