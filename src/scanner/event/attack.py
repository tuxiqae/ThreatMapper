from typing import Dict

import pendulum

from .location import Location
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["threatmapper_dev"]
attack_coll = mydb['attacks']


class Attack:
    def __init__(self, count: int,
                 attack_name: str,
                 attack_type: str,
                 source: Location,
                 destination: Location,
                 time: pendulum.DateTime = pendulum.now()):
        self.count = count
        self.name = attack_name
        self.category = attack_type
        self.source_location = source
        self.destination_location = destination
        self.time = time

    def __str__(self):
        return f"{{'count': {self.count}, 'name': {self.name}, 'type': {self.category}, 'time': {self.time}}}"


def attack_decoder(event: Dict):
    attack_coll.insert_one(event)
    # {'a_c': 4, 'a_n': 'Content Protection Violation', 'a_t': 'exploit', 'd_co': 'BE', 'd_la': 50.8336,
    # 'd_lo': 4.3337, 'd_s': 'BRU', 's_co': 'US', 's_lo': -119.7143, 's_la': 45.8491, 's_s': 'OR', 't': None}
    return Attack(count=event['a_c'],
                  attack_name=event['a_n'],
                  attack_type=event['a_t'],
                  source=Location(
        country=event["s_co"], state=event["s_s"], lon=event["s_lo"], lat=event["s_la"]),
        time=event['t'],
        destination=Location(country=event["d_co"], state=event["d_s"], lon=event["d_lo"], lat=event["d_la"]))
