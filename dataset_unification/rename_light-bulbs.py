import os


path = os.chdir("E:\\GarbageDatasets\\garbage_classification_9\\light-bulbs")


i = 1
for file in os.listdir(path):
    new_file_name = "light-bulbs{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
