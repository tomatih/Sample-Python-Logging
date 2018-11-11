import coloredlogs
import logging.config
import json

with open("logging.json", 'r') as f:
    logging.config.dictConfig(json.loads(f.read()))

logger = logging.getLogger("SampleLogger")
coloredlogs.install(level='INFO', logger=logger)

if __name__ == '__main__':
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
