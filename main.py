import os
current_folder = os.getcwd()

files = os.listdir(current_folder)

files_list = []

for file_name in files:
    if os.path.isfile(os.path.join(current_folder, file_name)):
        files_list.append(file_name)



file_names = []
file_extensions = []

for filename in files_list:
    name, extension = filename.split('.')
    file_names.append(name)
    file_extensions.append(extension)




file_name_number = []

for i in file_names:
    try:
        file_name_number.append(int(i))
    except:
        pass


print(file_name_number)


print(files_list)

file_name_number = sorted(file_name_number)


Old_File_Number = file_name_number[-1]

    


New_File_Number = Old_File_Number+1

print(Old_File_Number)
print(New_File_Number)

Old_file = open(f'{Old_File_Number}.txt', 'r')
content = Old_file.read()

Old_file.close()


New_File = open(f'{New_File_Number}.txt', 'w')


New_File.write(content)



New_File.close()



