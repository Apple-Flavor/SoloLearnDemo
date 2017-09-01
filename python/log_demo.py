import logging
import os

logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt'), filemode="w", level = logging.INFO)
logging.info("info"+"asdf")
logging.debug("debug")
logging.error("error")
