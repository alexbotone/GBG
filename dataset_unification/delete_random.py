import os
from random import sample

path = 'E:\\GarbageDatasets\\garbage_classification_del\\clothes'
#number_to_be_deleted_prevent_from_ delete = 3500

files = os.listdir(path)

print(len(files))

#for file in sample(files,number_to_be_deleted):
#    os.remove(path+"\\"+file)


files1 = os.listdir(path)
print(len(files1))
