#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sds011 import *
sensor = SDS011("/dev/ttyUSB0")
import datetime
import time
import requests
import json
#import pip
#!pip install python-aqi
import aqi
import warnings
warnings.filterwarnings("ignore")


# In[2]:


headers = {
    'QB-Realm-Hostname': 'builderprogram-dvijayakumar.quickbase.com',
    'User-Agent': 'raspberry-pi',
    'Authorization': 'QB-USER-TOKEN bz64sg_m2ax_dfuzmdhdke9qp6bf6zn2db9vtsep'
}


# In[3]:


# Turn-on sensor

print("Sensor reading...")
while True:
    sensor.sleep(sleep=False)
    time.sleep(10)
    # Turn-off sensor
    #sensor.sleep(sleep=True)
    pmt_2_5, pmt_10 = sensor.query()

    print(datetime.datetime.now())
    print("PM 2.5: "+str(pmt_2_5)+"\n PM 10: "+str(pmt_10))
    aqi_2_5=aqi.to_iaqi(aqi.POLLUTANT_PM25,str(pmt_2_5))
    aqi_10=aqi.to_iaqi(aqi.POLLUTANT_PM10,str(pmt_10))
    print("AQI 2.5: "+str(aqi_2_5))
    print("AQI 10: "+str(aqi_10))
    sensor.sleep(sleep=True)
    
    body = {"to":"bqytrwn8t","data":[{"7":{"value":aqi_2_5},"8":{"value":aqi_10},"10":{"value":"dinesh.vijayakumar@live.com"}}]}
    r = requests.post(
        'https://api.quickbase.com/v1/records', 
        headers = headers, 
        json = body,
        verify=False
        )
    #print(json.dumps(r.json(),indent=4))
    
    time.sleep(300)


# In[15]:





# In[ ]:




