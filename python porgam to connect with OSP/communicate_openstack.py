#!/usr/bin/python3

import sys

import requests


def api_communicator(end_point, method, api, token):
    try:
        response = requests.request(method=method, url=end_point + api, headers={"X-AUTH-TOKEN": token}, timeout=15)
    except Exception as e:
        print("Exception: ", e)
        return
    print(response.content)


param = sys.argv
if len(param) < 5:
    print("""
    Required param: end_point, method[GET | DELETE], api and token
    Syntax: python3 communicate_openstack.py <endpoint> <method> <API> <token>
    Example: python communicate_openstack.py  http://10.0.78.69/image GET /v2/images MGoSF3Ce7M8wsDnUrm6nPG
    """)
    exit(1)

api_communicator(param[1], param[2], param[3], param[4])
