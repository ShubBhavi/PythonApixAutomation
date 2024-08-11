import requests
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requestWrapper import post_request
from src.helpers.utilites import common_headers
from src.helpers.payload_manager import payload
from src.helpers.common_verifications import verify_status_code,verify_token
class Test_createBooking():
    #     url,header,paylaod,auth etc

    @pytest.mark.positive
    def test_create_booking_tc1(self):
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

    @pytest.mark.negative
    def test_create_booking_nobody_tc2(self):
        response=post_request(url=APIConstants.create_booking(),
                              headers=common_headers(),
                              auth=None,
                              payload={},
                              in_json=False
                              )
        verify_status_code(response_data=response,expected_data=500)
        print(response.status_code)








