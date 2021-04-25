from typing import Dict

import pendulum

from src.scanner.event.location import Location


class Attack:
    def __init__(self, count: int,
                 name: str,
                 category: str,
                 s_loc: Location,
                 d_loc: Location,
                 time: pendulum.DateTime = pendulum.now()):
        self.count = count
        self.name = name
        self.category = category
        self.source_location = s_loc
        self.destination_location = d_loc
        self.time = time

    def __str__(self):
        return f"{{'count': {self.count}, 'name': {self.name}, 'type': {self.category}, 'time': {self.time}"


def attack_decoder(event: Dict):
    return Attack(count=event['a_c'],
                  name=event['a_n'],
                  category=event['a_t'],
                  s_loc=Location(country=event["s_co"], state=event["s_s"], lon=event["s_lo"], lat=event["s_la"]),
                  d_loc=Location(country=event["d_co"], state=event["d_s"], lon=event["d_lo"], lat=event["d_la"]))
