import requests
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requestWrapper import post_request
from src.helpers.utilites import common_headers
from src.helpers.payload_manager import payload
from src.helpers.common_verifications import verify_status_code,verify_token
from jsonschema import validate
from jsonschema.exceptions import ValidationError
class Test_createBooking():
    #     url,header,paylaod,auth etc

    @pytest.mark.positive
    def test_create_booking_json_Schema(self):
        response=post_request(url=APIConstants.create_booking(),
                              headers=common_headers(),
                              auth=None,
                              payload=payload(),
                              in_json=False
                              )
        verify_status_code(response_data=response,expected_data=200)
        data=response.json()["bookingid"]
        print(data)
        verify_token(data)
        response_json=response.json()
        schema={
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "bookingid",
        "booking"
    ],
    "properties": {
        "bookingid": {
            "type": "integer",
            "default": 0,
            "title": "The bookingid Schema",
            "examples": [
                2539
            ]
        },
        "booking": {
            "type": "object",
            "default": {},
            "title": "The booking Schema",
            "required": [
                "firstname",
                "lastname",
                "totalprice",
                "depositpaid",
                "bookingdates",
                "additionalneeds"
            ],
            "properties": {
                "firstname": {
                    "type": "string",
                    "default": "",
                    "title": "The firstname Schema",
                    "examples": [
                        "Sally"
                    ]
                },
                "lastname": {
                    "type": "string",
                    "default": "",
                    "title": "The lastname Schema",
                    "examples": [
                        "Brown"
                    ]
                },
                "totalprice": {
                    "type": "integer",
                    "default": 0,
                    "title": "The totalprice Schema",
                    "examples": [
                        111
                    ]
                },
                "depositpaid": {
                    "type": "boolean",
                    "default": False,
                    "title": "The depositpaid Schema",
                    "examples": [
                        True
                    ]
                },
                "bookingdates": {
                    "type": "object",
                    "default": {},
                    "title": "The bookingdates Schema",
                    "required": [
                        "checkin",
                        "checkout"
                    ],
                    "properties": {
                        "checkin": {
                            "type": "string",
                            "default": "",
                            "title": "The checkin Schema",
                            "examples": [
                                "2013-02-23"
                            ]
                        },
                        "checkout": {
                            "type": "string",
                            "default": "",
                            "title": "The checkout Schema",
                            "examples": [
                                "2014-10-23"
                            ]
                        }
                    },
                    "examples": [{
                        "checkin": "2013-02-23",
                        "checkout": "2014-10-23"
                    }]
                },
                "additionalneeds": {
                    "type": "string",
                    "default": "",
                    "title": "The additionalneeds Schema",
                    "examples": [
                        "Breakfast"
                    ]
                }
            },
            "examples": [{
                "firstname": "Sally",
                "lastname": "Brown",
                "totalprice": 111,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2013-02-23",
                    "checkout": "2014-10-23"
                },
                "additionalneeds": "Breakfast"
            }]
        }
    },
    "examples": [{
        "bookingid": 2539,
        "booking": {
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
    }]
}
        try:
            validate(instance=response_json,schema=schema)
        except ValidationError as e:
            print(e.message)