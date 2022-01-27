#/Users/User/Documents/

import os.path
import shutil

path = "/Users/User/Documents/A_Sefu/A/B"

af = os.path.exists(path)

if not af:
    os.makedirs(path)
    print("The new directory is created.")

print("Now we create the buba.txt file in the A folder")
print("Press \\ ENTER \\ to continue.")

y = input()

tpath ="/Users/User/Documents/A_Sefu/A"
buba = "buba"
complete_n = os.path.join(tpath, buba+".txt")
file1 = open(complete_n, "w")

print("Now write what you want into the field")
typee = input()

file1.write(typee)

file1.close()

print("....Done")
print("Now we move the buba.txt from the A folder to the B folder.")
print("Press \\ ENTER \\ to continue.")

y2 = input()

srcf = r"/Users/User/Documents/A_Sefu/A/buba.txt"
desf = r"/Users/User/Documents/A_Sefu/A/B/buba.txt"

shutil.move(srcf , desf)

print("\\ DONE \\")