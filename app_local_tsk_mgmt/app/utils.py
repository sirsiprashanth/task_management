from passlib.context import CryptContext
from twilio.rest import Client
from dotenv import load_dotenv
import os

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

def pwd_hashing(password_val):
    if password_val:
        return pwd_context.hash(password_val)
    return None

def validate_pw(password, hash_pw):
    return pwd_context.verify(password, hash_pw)



def phone_otp_validate(cust_num):

    load_dotenv('/Users/guruprasadsirsi/Documents/Python_files/task-managment-master/env/.env')

    Account_SID = os.getenv('Twilio_Account_SID')
    Auth_token = os.getenv('Twilio_Auth_token' )
    Verification_SID = os.getenv("Twilio_Verification_Service_SID")

    print(f'Twilio_Verification_Service_SID : {Verification_SID}')

    client = Client(Account_SID, Auth_token)

    # message = client.messages.create(body = 'Hello World', from_ = Twilio_Phone_Number, to= cust_phone_num)

    verify = client.verify.services(Verification_SID)
    otp_send = verify.verifications.create(to=cust_num, channel='sms')
    print(f'Send status : {otp_send.status}')

    code_ = input('Please enter the OTP: ')
    result = verify.verification_checks.create(to=cust_num, code=code_)

    if result.status == 'approved':
        return result.status
    else:
        new_code = input('Incorrect OTP. Please re-enter the correct OTP: ')
        result = verify.verification_checks.create(to=cust_num, code=new_code)





    