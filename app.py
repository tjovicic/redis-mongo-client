from flask import Flask
import redis
from bson import json_util

from config import *
from mongo_client import Mongo

app = Flask(__name__)
mongo_client = Mongo()
redis_client = redis.Redis.from_url(REDIS_DSN)


@app.route('/')
def healthy():
    return "OK", 200


@app.route('/collection/<collection>/id/<document_id>')
def fetch(collection, document_id):
    return get_from_cache_or_mongo(collection, document_id), 200


def get_from_cache_or_mongo(collection, document_id):
    key = f'mongodb:{collection}:{document_id}'
    result = get_from_cache(key)

    if result is None:
        result = mongo_client.find_one(collection, document_id)
        redis_client.set(key, json_util.dumps(result))

    return result


def get_from_cache(key):
    result = redis_client.get(key)

    if result is None:
        return result

    return json_util.loads(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG_MODE)
