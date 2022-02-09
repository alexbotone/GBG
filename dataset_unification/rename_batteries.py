import os


#path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\cardboard")
path = os.chdir("E:\\GarbageDatasets\\garbage_classification_9\\batteries")

i=946
for file in os.listdir(path):
    new_file_name = "battery{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
