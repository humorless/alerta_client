#!/usr/bin/env python

import requests
import time
import json


url = "http://10.20.30.40:8181/api/alert"

event="fastmedia.worker.process > 90"
resource="gwb-sh-140.112.18.71"
origin="owl"
status="open"
d = {
    "event": event,
    "resource": resource,
    "environment": "Production",
    "service": ["none"],
    "origin": origin,
    "status": status
}

r = requests.post(url, data=json.dumps(d))
print r.text
