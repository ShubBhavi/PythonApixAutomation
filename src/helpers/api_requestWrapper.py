# to make get patch put post
import json
import requests


def get_request(url,auth,in_json):
    response=requests.get(url=url,auth=auth,json=in_json)
    if in_json is True:
        return response.json()
    return response


def post_request(url,auth,in_json,headers,payload):
    response=requests.post(url=url,auth=auth,json=in_json,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

def patch_request(url,auth,in_json,headers,payload):
    response=requests.patch(url=url,auth=auth,json=in_json,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

def put_request(url,auth,in_json,headers,payload):
    response=requests.put(url=url,auth=auth,json=in_json,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

def delete_request(url,auth,in_json,headers,payload):
    response=requests.delete(url=url,auth=auth,json=in_json,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

