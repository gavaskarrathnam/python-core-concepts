import os
from datetime import datetime

now = datetime.now()

file_name = now.strftime("%b") + ".txt"
dir_name = now.strftime("%Y")
os.makedirs(dir_name, exist_ok=True)

file_name_with_path = os.getcwd() + "\\" + now.strftime("%Y") + "\\" + file_name

open_file = open(file_name_with_path, 'a+')
open_file.write("Testing... Testing... Testing...Testing...")
open_file.close()
