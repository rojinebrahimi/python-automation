#Dec/14/2020 
#Rojin Ebrahimi

import re
import sys

# open the image file and convert it into string format
def img(file):
    string = ''
    image_name = sys.argv[2]
    with open(file, 'rb') as f:
        bin_val = f.read(1)
        string += "flash unsigned char "+ image_name +"[]=\n{\n"
        while len(bin_val) != 0:
            hex_val = hex(ord(bin_val))
            string += hex_val + ', '
            bin_val = f.read(1)
        string += "\n};"
    with open(f"{image_name}.c", "w") as fout:
        fout.write(string)
        fout.close()
        print(f"Hex Code Created For {image_name}!")
    

img(str(sys.argv[1]))

