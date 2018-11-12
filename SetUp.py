import coloredlogs
import logging.config
import json

def GetLogger():
    with open("logging.json", 'r') as f:
        logging.config.dictConfig(json.loads(f.read()))

    logger = logging.getLogger("SampleLogger")
    coloredlogs.install(level='INFO', logger=logger)
    return logger