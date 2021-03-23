import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config.config import config


def mongoConnect():
    try:
        client = MongoClient(config["mongoHost"], username=config["mongoUser"],
                             password=config["mongoPassword"], authSource=config["mongoAuthDB"])

        # server_info() ensures a connection to the DB is established
        logging.info(client.server_info())
        return client
    except ServerSelectionTimeoutError:
        logging.error("Could not connect to mongo DB")
