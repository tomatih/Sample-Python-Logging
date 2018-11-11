import coloredlogs
import logging.config
import json

with open("logging.json", 'r') as f:
    logging.config.dictConfig(json.loads(f.read()))

logger = logging.getLogger("SampleLogger")
coloredlogs.install(level='INFO', logger=logger)

if __name__ == '__main__':
    logger.debug("Debug Message")
    logger.info("Info Message")
    logger.warning("A Warning")
    logger.error("Error Message")
    logger.critical("Critical Error Message")
