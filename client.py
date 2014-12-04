#!/usr/bin/env python

import argparse
import requests
import sys

host = 'http://localhost:8080'

def create_data(data):
    result = requests.post(host, data)
    return result.status_code, result.text

def get_data(id):
    result = requests.get(host + '/' + id)
    return result.status_code, result.text

def list_data():
    result = requests.get(host)
    return result.status_code, result.text

def delete_data(id):
    result = requests.delete(host + '/' + id)
    return result.status_code, result.text


parser = argparse.ArgumentParser(description='Demo Client')
subparsers = parser.add_subparsers()

parser_create = subparsers.add_parser('create')
parser_create.add_argument('data')
parser_create.set_defaults(func=create_data)

parser_get = subparsers.add_parser('get')
parser_get.add_argument('id')
parser_get.set_defaults(func=get_data)

parser_list = subparsers.add_parser('list')
parser_list.set_defaults(func=list_data)

parser_delete = subparsers.add_parser('delete')
parser_delete.add_argument('id')
parser_delete.set_defaults(func=delete_data)


if len(sys.argv) > 1:
    args = vars(parser.parse_args())
else:
    sys.argv.append('-h')
    parser.parse_args()

func = args['func']
del args['func']

print func(**args)
