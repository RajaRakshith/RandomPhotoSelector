import os
import shutil
from random import randint

list_of_all_files = os.listdir("/Volumes/USB DISK/Google Photos/Family")
count_of_supported_images = 0

list_of_sifted_files = []
list_of_indexes=[]

list_of_final_thousand_files = []

iterations=0


for file in list_of_all_files:
    if file.endswith(".JPG"):
        count_of_supported_images+=1
        list_of_sifted_files.append(str(file))
    elif file.endswith(".jpg"):
        count_of_supported_images+=1
        list_of_sifted_files.append(str(file))
    elif file.endswith(".HEIC"):
        count_of_supported_images+=1
        list_of_sifted_files.append(str(file))
    elif file.endswith(".heic"):
        count_of_supported_images+=1
        list_of_sifted_files.append(str(file))
    else:
        print(str(file) + "BAD")
    iterations+=1

    if iterations%1000==0:
        print("1000 DONE----------------------------------")
        print(iterations)
    

    

print(list_of_sifted_files)
print(len(list_of_sifted_files))

for x in range(0,1000):
    current_random=randint(1,len(list_of_sifted_files))
    if current_random in list_of_indexes:
        while current_random in list_of_indexes:
            current_random=randint(1,len(list_of_sifted_files))
    list_of_indexes.append(current_random)

for item in list_of_indexes:
    list_of_final_thousand_files.append(list_of_sifted_files[item])

for file in list_of_final_thousand_files:
    source='/Volumes/USB DISK/Google Photos/Family/' + str(file)
    destination = "/Volumes/USB DISK/Google Photos/thousand_photos/" + str(file)
    shutil.copyfile(source, destination)


    
        
"""
for x in range(0,1000):
    list_of_random_increments.append(
"""
