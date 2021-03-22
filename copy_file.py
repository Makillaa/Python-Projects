# Implementation of creating a copy of existing files
filename1 = input('Which file to copy?:')
filename2 = 'copy_' + filename1 #rename of the copied file

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')

file2.write(file1.read()) #writing content from original to copy

file1.close
file2.close
print('File ' + str(filename1) + ' copied successfully!') 