import logging
import pendulum

import scanner


def main():
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

    start_time = pendulum.now()
    logging.info("--Started--")

    event_generator = scanner.checkpoint_event_generator()

    for event_data in event_generator:
        logging.info(event_data)

    end_time = pendulum.now()
    logging.info("Took %s", (end_time - start_time).as_interval())


if __name__ == '__main__':
    main()
