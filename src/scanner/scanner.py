import requests
from queue import Queue
import json

q: Queue = Queue()


def event_generator():
    r = requests.get(r"https://threatmap-api.checkpoint.com/ThreatMap/api/feed", stream=True)
    for chunk in r.iter_lines(decode_unicode=True, delimiter="\n\n"):
        if len(chunk) > 0 and chunk[0] == "e":
            chunk_by_lines = chunk.split("\n")
            if chunk_by_lines[0] == "event:attack":
                yield json.loads(chunk_by_lines[1].split(":", maxsplit=1)[1])


def scanner_main():
    eg = event_generator()
