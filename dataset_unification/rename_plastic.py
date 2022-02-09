import os


#path = os.chdir("E:\\GarbageDatasets\\garbage_classification_9\\plastic")
path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\plastic")


#i = 866
i = 2107
for file in os.listdir(path):
    new_file_name = "plastic{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
