import os 

path = os.chdir("C:\\Users\Katleho Phate\\Documents\\LazyList\\LazyList")

i = 0
for file in os.listdir(path):

   new_file_name = "calculator{}.py".format(i)
   os.rename(file, new_file_name)
   i = i +1
