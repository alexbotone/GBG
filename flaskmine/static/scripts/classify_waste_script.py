from flaskmine.application.util import classify_waste, load_artifacts
import requests

accepted_formats = ('.png', '.jpg', '.jpeg')
#url = 'http://127.0.0.1:5000/api/classifywaste'
url = 'http://gbgselection.ro//api/classifywaste'


def validate_file(file_path):
    if file_path.endswith(accepted_formats):
        return True
    else:
        print("invalid format")
        return False


filename = input("File path: ")

if validate_file(filename):
    files = {'files[]': open(filename, 'rb')}
    response = requests.post(url, files=files)
    print(response.status_code)
    print(response.json())

else:
    print("Please try again!")
    filename = input("File path: ")

