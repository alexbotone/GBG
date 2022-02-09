import os


#path = os.chdir("E:\\GarbageDatasets\\garbage_classification_9\\metal")
path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\metal")


#i = 770
i = 1862
for file in os.listdir(path):
    new_file_name = "metal{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
