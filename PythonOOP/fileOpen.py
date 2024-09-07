fh = open('poem.txt', 'rt', encoding='utf8')

for line in fh.readlines():
    print(line.strip())# removes the trailing and preceeding white spaces in the lines

fh.close()

# delete the file
# we use the os.remove()
# import the os module
import os
if os.path.exists('poem.txt'):
    os.remove('poem.txt')

else:
    print('File does not exist')