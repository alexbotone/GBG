import os


#path = os.chdir("E:\\GarbageDatasets\\garbage_classification_9\\paper")
path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\paper")


#i = 1051
i = 2112
for file in os.listdir(path):
    new_file_name = "paper{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
