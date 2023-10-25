import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime

# Globale Variable für die MongoDB-Verbindung
db_client = None


def connect_to_db():
    global db_client
    if db_client is None:
        try:
            mongo_user = os.environ.get("MONGODB_USERNAME")
            mongo_pass = os.environ.get("MONGODB_PASSWORD")
            mongo_host = os.environ.get("MONGODB_HOSTNAME")
            mongo_port = os.environ.get("MONGODB_PORT")
            mongo_db = os.environ.get("MONGODB_DATABASE")

            if not all([isinstance(v, str) for v in [mongo_user, mongo_pass, mongo_host, mongo_db]]):
                raise ValueError("All MongoDB settings must be provided as strings.")

            db_client = MongoClient(f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/{mongo_db}?authMechanism=DEFAULT",
                                    maxPoolSize=50)[mongo_db]
        except (ConnectionFailure, ValueError) as e:
            print(f"Could not connect to MongoDB, retrying... {e}")
            db_client = None


def save_data(price, ticker):
    if db_client is None:
        connect_to_db()  # Versucht, die Verbindung herzustellen oder wiederherzustellen
    if db_client is not None:
        collection = db_client['Prices']
        timestamp = datetime.utcnow().isoformat()

        collection.update_one(
            {'ticker': ticker},
            {'$push': {'data': {'price': price, 'timestamp': timestamp}}},
            upsert=True
        )


# Verbindung beim Start der Anwendung initialisieren
connect_to_db()