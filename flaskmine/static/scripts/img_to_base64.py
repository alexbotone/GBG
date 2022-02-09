import base64

accepted_formats = ('.png', '.jpg', '.jpeg')


def create_base64_file():
    f = open(new_file_path, 'wb')
    print('Success! your file is here:' + new_file_path)
    f.write(byteform)
    f.close()


def validate_file(file_path):
    if file_path.endswith(accepted_formats):
        return True
    else:
        print("invalid format")
        return False


filename = input("File path: ")

while True:
    try:
        with open(filename, 'rb') as imagefile:
            byteform = base64.b64encode(imagefile.read())
            new_file_path = filename.replace('png', 'bin').replace('jpg', 'bin').replace('jpeg', 'bin')
            if validate_file(filename):
                create_base64_file()
            filename = input("File path or type 'exit' to close: ")
    except:
        if filename == 'exit':
            break
        else:
            print('Fisierul nu exista!')
            filename = input("File path or type 'exit' to close: ")
if validate_file(filename):
    response = requests.post('http://127.0.0.1:5000/classifywaste',filename)
elif validate_file(filename) == 'output.bin':
    response = requests.post('http://127.0.0.1:5000/classifywaste','output.bin')
else:
    print("Please try again!")
    response = None


