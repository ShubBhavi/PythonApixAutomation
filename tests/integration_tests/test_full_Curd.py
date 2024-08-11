import requests
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requestWrapper import post_request,put_request,delete_request
from src.helpers.utilites import common_headers,common_token_header,common_auth_header
from src.helpers.payload_manager import payload,token_payload
from src.helpers.common_verifications import verify_status_code,verify_token,verify_json_key_for_not_null


class Test_createBooking():
    #     url,header,paylaod,auth etc

    @pytest.fixture()
    def test_create_token_tc1(self):
        response=post_request(url=APIConstants.create_token(),
                              payload=token_payload(),
                              auth=None,
                              in_json=None,
                              headers=common_headers()
                              )
        verify_status_code(response_data=response,expected_data=200)
        token=response.json()["token"]
        print(token)
        verify_token(token)
        return token


    @pytest.fixture()
    def test_create_booking_tc2(self):
        response = post_request(url=APIConstants.create_booking(),
                                headers=common_headers(),
                                auth=None,
                                payload=payload(),
                                in_json=False
                                )
        verify_status_code(response_data=response, expected_data=200)
        booking_id= response.json()["bookingid"]
        print(booking_id)
        verify_json_key_for_not_null(booking_id)
        return booking_id


    #we need token for update and booking id as well we need
    def test_update_booking_tc3(self,test_create_token_tc1,test_create_booking_tc2):
        token=test_create_token_tc1
        booking_id=test_create_booking_tc2
        # headers=common_token_header(token)
        # print(headers)
        # print(token)
        # print(booking_id)
        response = put_request(url=APIConstants.put_patch_delete(booking_id),
                               headers=common_auth_header(),
                               auth=None,
                               payload=payload(),
                               in_json=False
                               )
        verify_status_code(response_data=response, expected_data=200)

    def test_delete_booking_tc4(self,test_create_token_tc1,test_create_booking_tc2):
        booking_id=test_create_booking_tc2
        token=test_create_token_tc1
        print(token)
        # headers=common_token_header(token)
        # print(headers)
        # print(token)
        print(booking_id)
        response = delete_request(url=APIConstants.put_patch_delete(booking_id),
                               headers=common_auth_header(),
                               auth=None,
                               payload={},
                               in_json=False
                               )
        verify_status_code(response_data=response, expected_data=201)