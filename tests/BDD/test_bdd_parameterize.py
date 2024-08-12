import pytest
import requests
import openpyxl
from src.constants.api_constants import APIConstants
from src.helpers.utilites import common_headers
from src.helpers.common_verifications import verify_status_code


# 1read the excel file and put them in an array []

# return data which has username and password
def read_creds_from_excel(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        # whatever we are getting in row we are storing username and password
        username,password=row
        credentials.append({"username":username,"password":password})
    return credentials



def make_request_auth(username,password):
    payload={
        "username":username,
        "password":password
    }
    headers = {"Content-Type": "application/json"}

    response=requests.post(url=APIConstants.create_token(),
                           json=payload,
                           headers=common_headers()
                           )
    data=response.json()
    return response

@pytest.mark.parametrize("user_cred",read_creds_from_excel(r"C:\Users\233004\PycharmProjects\newprojj\PythonApixAutomation\tests\BDD\test_ddt.xlsx"))
def test_create_token(user_cred):
        username=user_cred["username"]
        psssword=user_cred["password"]
        print(username,psssword)
        response=make_request_auth(username=username,password=psssword)
        # if response.json()["token"] is not None:
        #     print("token is present")
        # else:
        #     print("bad credentials")
        print(response)



# we have to run the make request auth for the rows we have in the excel






