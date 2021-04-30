import json
import requests

from event import attack_decoder

URL = r"https://threatmap-api.checkpoint.com/ThreatMap/api/feed"


def checkpoint_event_generator():
    with requests.Session() as session:
        while True:
            stream: requests.Response = session.get(URL, stream=True)

            for event in stream.iter_lines(decode_unicode=True, delimiter="\n\n"):
                if len(event) == 0:  # Discard of empty events
                    continue

                event_props = dict()

                for line in event.split("\n"):
                    key, val = line.split(":", maxsplit=1)
                    event_props[key] = val

                if event_props.get("event") == "attack":
                    yield json.loads(event_props["data"], object_hook=attack_decoder)
            # TODO: Add `finally`
