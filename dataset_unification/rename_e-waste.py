import os


path = os.chdir("E:\\GarbageDatasets\\garbage_classification_9\\e-waste")


i = 1
for file in os.listdir(path):
    new_file_name = "e-waste{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
