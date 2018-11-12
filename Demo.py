import SetUp
logger = SetUp.GetLogger()

if __name__ == '__main__':
    logger.debug("Debug Message")
    logger.info("Info Message")
    logger.warning("A Warning")
    logger.error("Error Message")
    logger.critical("Critical Error Message")
