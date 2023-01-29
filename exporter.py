import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
import requests
import json
from collections import Counter

class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        file_name = "/app/log/user.log"

        file = open(file_name, "r")
        data = []


        for line in file.readlines():
            details = line.split("|")
            details = [x.strip() for x in details]
            address= details[4]
            json_object = json.loads(address)

            for k ,v  in json_object["request"].items():
                if k == "address":
                    data.append(v)

        a = dict(Counter(data))

        list_of_metrics = [{'address': k, 'value':v} for k,v in a.items()]
        for key in list_of_metrics:
           print(key)
           g = GaugeMetricFamily("request_addresses", 'Help text', labels=['datalnddev'])
           g.add_metric([str(key['address'])], key['value'])
           yield g

if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)
