import adafruit_dht
import time
import board
import json
import requests

# --------- User Settings ---------
headers = {
    'QB-Realm-Hostname': 'builderprogram-dvijayakumar.quickbase.com',
    'User-Agent': 'raspberry-pi',
    'Authorization': 'QB-USER-TOKEN bz64sg_m2ax_dfuzmdhdke9qp6bf6zn2db9vtsep'
}
MINUTES_BETWEEN_READS = 5
METRIC_UNITS = True
# ---------------------------------

dhtSensor = adafruit_dht.DHT22(board.D4)
print(dhtSensor)

while True:
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
        print(temp_c)
    except RuntimeError:
        print("RuntimeError, trying again...")
        continue
    humidity = format(humidity,".2f")       
    if METRIC_UNITS:
        body = {"to":"bqxbme8m4","data":[{"6":{"value":temp_c},"10":{"value":1},"12":{"value":humidity}}]}
    else:
        temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")
        body = {"to":"bqxbme8m4","data":[{"6":{"value":temp_f},"10":{"value":1},"12":{"value":humidity}}]}
            
    r = requests.post(
    'https://api.quickbase.com/v1/records', 
    headers = headers, 
    json = body
    )
    print(json.dumps(r.json(),indent=4))
    print(humidity)
    print(temp_c)
    time.sleep(60*MINUTES_BETWEEN_READS)
