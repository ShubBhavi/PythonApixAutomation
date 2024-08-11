# Https verification status code


def verify_status_code(response_data,expected_data):
    assert response_data.status_code==expected_data,"expected status code is "


# verification of response body
# example like token

def verify_json_key_for_not_null(key):
    assert key!=0,"key is not empty"
    assert key>0,"key is greater than zero"

def verify_token(key):
    assert key is not None