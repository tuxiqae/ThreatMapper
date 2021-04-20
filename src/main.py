import scanner
import logging

if __name__ == '__main__':
    eg = scanner.event_generator()

    for event_data in eg:
        print(event_data)
