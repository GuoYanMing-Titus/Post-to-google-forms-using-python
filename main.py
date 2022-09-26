import requests
import time
import datetime

url = 'https://docs.google.com/forms/u/0/d/e/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/formResponse'
email = '%%%%%%%%%%%%%%%@gmail.com'
name = '%%%%%%%%%%%%'
student_id = '16'
sign_list = [
    'Sign in in the morning', 
    'Sign out in the morning', 
    'Sign in in the afternoon',
    'Sign out in the afternoon'
] 
sign_data = sign_list[3] 


def get_login_values():
    now = str(datetime.datetime.now())
    now = now.split(' ')[0] # YYYY-MM-DD
    values = {
        'entry.1065046570':now,
        'entry.1166974658':student_id,
        'entry.2005620554':name,
        'entry.839337160':'test_by_python_0', # annotation
        'entry.1740806700':sign_data,
        'emailAddress':email,
    }
    return values

def send_attendance(url, data):
    try:
        response = requests.post(url, data=data)
        print(repr(data))
        if response.status_code != 200:
            print(repr(response))
            print("Error Occured!")
            return
        print("Form Submiting...")
        time.sleep(2)
        print("Form Submitted.")
    except:
        print("Error Occured!")


final_data = get_login_values()
send_attendance(url, final_data)
