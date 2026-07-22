import json,random,time
from datetime import datetime
while True:
 d={"silver":round(42+random.uniform(-.5,.5),2),
    "gold":round(3430+random.uniform(-10,10),2),
    "platinum":round(1490+random.uniform(-10,10),2),
    "updated":datetime.now().isoformat()}
 open("prices.json","w").write(json.dumps(d))
 time.sleep(15)
