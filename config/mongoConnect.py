from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config.config import config


def mongoConnect():
    try:
        client = MongoClient(config["mongoHost"], username=config["mongoUser"],
                             password=config["mongoPasswd"], authSource=config["mongoAuthDB"])
        info = client.server_info()
        return client
    except ServerSelectionTimeoutError:
        print("Could not connect to mongo DB")
