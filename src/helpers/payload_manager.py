# payload for create booking


def payload():
    payload={
    "firstname": "Sally",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
}
    return payload

def token_payload():
    payload={
    "username" : "admin",
    "password" : "password123"
}
    return payload