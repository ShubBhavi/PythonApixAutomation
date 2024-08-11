# common headers

def common_headers():
    headers={"Content-Type":"application/json"}
    return headers

def common_token_header(token):
    headers = {"Content-Type": "application/json",
               "Cookie":token
               }
    return headers


def common_auth_header():
    headers = {"Content-Type": "application/json",
               "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="
               }
    return headers

