#/Users/User/Documents/

import os.path
import shutil

path1 = "/Users/User/Documents/A_Sefu/A"

af = os.path.exists(path1)

if not af:
    os.makedirs(path1)
    print("The new A directory is created.")


path2 = "/Users/User/Documents/A_Sefu/B"

af = os.path.exists(path2)

if not af:
    os.makedirs(path2)
    print("The new B directory is created.")

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
desf = r"/Users/User/Documents/A_Sefu/B/buba.txt"

shutil.move(srcf , desf)

print("\\ DONE \\")
