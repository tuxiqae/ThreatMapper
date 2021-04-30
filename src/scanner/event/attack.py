from typing import Dict

import pendulum

from .location import Location

from database import attack_coll


class Attack:
    def __init__(self,
                 count: int,
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
    rename_dict = {'a_c': 'count',
                   'a_n': 'attack_name',
                   'a_t': 'attack_type',
                   's_co': 'src_country',
                   's_s': 'src_state',
                   's_lo': 'src_lon',
                   's_la': 'src_lat',
                   'd_co': 'dst_country',
                   'd_s': 'dst_state',
                   'd_lo': 'dst_lon',
                   'd_la': 'dst_lat',
                   't': 'time'
                   }
    event = dict((rename_dict[key], value) for (key, value) in event.items())

    event["time"] = pendulum.now()

    attack_coll.insert_one(event)
    # {'a_c': 4, 'a_n': 'Content Protection Violation', 'a_t': 'exploit', 'd_co': 'BE', 'd_la': 50.8336,
    # 'd_lo': 4.3337, 'd_s': 'BRU', 's_co': 'US', 's_lo': -119.7143, 's_la': 45.8491, 's_s': 'OR', 't': None}
    return Attack(count=event['count'],
                  attack_name=event['attack_name'],
                  attack_type=event['attack_type'],
                  source=Location(
                      country=event["src_country"], state=event["src_state"], lon=event["src_lon"],
                      lat=event["src_lat"]),
                  time=event['time'],
                  destination=Location(country=event["dst_country"], state=event["dst_state"], lon=event["dst_lon"],
                                       lat=event["dst_lat"]))
