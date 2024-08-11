# adding constants

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def create_token():
        return "https://restful-booker.herokuapp.com/auth"


# for put,patch,delete
#     all of the testcases will be having booking id diff so we dont have static method
    def put_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
