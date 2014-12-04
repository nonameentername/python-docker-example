import json
import os
from bottle import default_app
from bottle import delete
from bottle import get
from bottle import post
from bottle import request
from bottle import response
from bottle import route
from bottle import run
from riak import RiakClient


def get_bucket():
    if 'RIAK_PORT_8098_TCP_ADDR' in os.environ:
        riak = RiakClient('http', host=os.environ['RIAK_PORT_8098_TCP_ADDR'])
    else:
        riak = RiakClient('http')
    return riak.bucket('apps')

def create(data):
    obj = get_bucket().new(data=data)
    obj.store()
    return obj.key

@post('/')
def create_data():
    data = request.body.read()
    return create(data)

@get('/<id>')
def get_data(id):
    data = get_bucket().get(id)
    if data.data:
        return data.data
    else:
        response.status = 404
        return ''

@delete('/<id>')
def delete_data(id):
    data = get_bucket().get(id)
    if data.data:
        data.delete()
    else:
        response.status = 404
        return ''

@get('/')
def list_data():
    return json.dumps(get_bucket().get_keys())

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, reloader=True, server='paste')
else:
    application = default_app()
