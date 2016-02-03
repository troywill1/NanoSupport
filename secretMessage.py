# lesson 3.2: Use functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are, you have to
# remove all numbers from the files in a folder called prank. But this will
# be so tedious to do! Get Python to do it for you!

# Use this space to describe your approach to the problem
# 1. For each file in a folder
# 2. Read in the filename
# 3. Strip any numbers from the filename
# 4. Rename the file
# 5. Exit

# Your code here.
import os

def rename_files():
    # Get filenames from a folder
    file_list = os.listdir(r"C:\Users\troyw\Documents\testFiles") # create a list of dir items
                                            # 'r' evaluates string as-is
    print file_list
    saved_path = os.getcwd() # get current working directory
    print "Current Working Directoy is " + saved_path

    # For each filename, rename filename
    for file_name in file_list:
        # rename the file using string.translate
        print "Old Name - " + file_name
        print "New Name - " + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
        os.chdir(saved_path)

rename_files()
