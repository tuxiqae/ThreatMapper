import pendulum

import scanner
import logging


def main():
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

    start_time = pendulum.now()
    logging.info("--Started--")

    eg = scanner.checkpoint_event_generator()

    for event_data in eg:
        logging.info(event_data)

    end_time = pendulum.now()
    logging.info(f"Took {(end_time - start_time).as_interval()}")


if __name__ == '__main__':
    main()
