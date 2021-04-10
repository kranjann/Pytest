import logging


def test_loggingDemo()  :
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler class object

    logger.setLevel(logging.INFO)
    logger.debug("This is a debug statement")
    logger.info("This is an info statement")
    logger.warning("This is a warning statement")
    logger.error("This is an error statement")
    logger.critical("This is a critical statement")
