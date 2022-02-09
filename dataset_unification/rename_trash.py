import os


path = os.chdir("E:\\GarbageDatasets\\garbage_classification_6\\trash")


i = 698
for file in os.listdir(path):
    new_file_name = "trash{}.jpg".format(i)
    os.rename(file, new_file_name)
    i= i+1
