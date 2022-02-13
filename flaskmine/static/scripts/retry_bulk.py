import requests
import time

accepted_formats = ('.png', '.jpg', '.jpeg', 'exit')
# url = 'http://127.0.0.1:5000/api/classifywaste'
url = 'http://gbgselection.ro:80/api/classifywaste'


def validate_file(file_path):
    if file_path.endswith(accepted_formats):
        return True
    else:
        print("invalid format")
        return False


filename = input("File path: ")

while filename is not None:
    try:
        if validate_file(filename):
            files = {'files[]': open(filename, 'rb')}
            response = requests.post(url, files=files)
            print(response.status_code)
            print(response.json())
            filename = input("File path or type 'exit' to close: ")
        else:
            print("Please try again!")
            filename = input("File path or type 'exit' to close: ")
    except:
        if filename.startswith('exit'):
            break
        else:
            print('Fisierul nu exista!')
            filename = input("File path or type 'exit' to close: ")
