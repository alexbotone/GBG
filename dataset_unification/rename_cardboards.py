import os


#path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\cardboard")
path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\cardboard")

i=892
for file in os.listdir(path):
    new_file_name = "cardboard{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
