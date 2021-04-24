import logging

import requests
import json

URL = r"https://threatmap-api.checkpoint.com/ThreatMap/api/feed"


def checkpoint_event_generator():
    with requests.Session() as session:
        while True:
            stream: requests.Response = session.get(URL, stream=True)

            for event in stream.iter_lines(decode_unicode=True, delimiter="\n\n"):
                if len(event) > 0:

                    chunk_by_lines = event.split("\n")
                    if chunk_by_lines[0][-1] == "k":  # Event type ends with "k" -- "attack"
                        yield json.loads(chunk_by_lines[1].split(":", maxsplit=1)[1])
            logging.warning("----DISCONNECTED----")  # TODO: Remove
            # TODO: Add `finally`
