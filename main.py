import csv
from collections import defaultdict
from datetime import datetime

def run(path='data/shipments.csv'):
    groups=defaultdict(list); exceptions=[]
    with open(path,newline='') as f:
        for r in csv.DictReader(f):
            expected=datetime.fromisoformat(r['promised_at'])
            delivered=datetime.fromisoformat(r['delivered_at']) if r['delivered_at'] else None
            late=(delivered>expected) if delivered else True
            groups[r['station']].append(not late)
            if late: exceptions.append(r['shipment_id'])
    return {'station_on_time_pct':{k:round(100*sum(v)/len(v),1) for k,v in sorted(groups.items())}, 'exception_shipments':exceptions}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
