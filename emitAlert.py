#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import json


apiKey = 'nskKwHlzEIuTejKqcYKT7-IB_owdw7Dd8sGhXceA'
headers={'Authorization':'Key '+ apiKey}

url = "http://10.20.30.40:8181/api/alert"

event="slowmedia.worker.process > 90"
value="99.5"
resource="gwb-sh-140.112.18.71"
text="央视直播 is down"
severity="major"
status="open"
attributes={"idc":"重庆联通-西南数据中心","platform":"c01.i07","contact":"負責人","phone":"158000000000"}
createTime="2017-02-07T08:57:23.654Z"
origin="owl"
correlate=["slowmedia.worker.process > 90", "slowmedia.worker.process > 95"]
rawData="All the other details"
d = {
    "event": event,
    "value": value,
    "resource": resource,
    "text": text,
    "severity": severity,
    "status": status,
    "attributes": attributes,
    "createTime": createTime,
    "origin": origin,
    "correlate": correlate,
    "rawData": rawData
}

r = requests.post(url, data=json.dumps(d), headers=headers)
print r.text



d2 = d
d2["event"]="slowmedia.worker.process > 95"
r = requests.post(url, data=json.dumps(d2), headers=headers)
print r.text
