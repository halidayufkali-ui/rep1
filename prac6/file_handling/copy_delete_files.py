import shutil
import os

# Copy file
shutil.copy("example.txt", "copy_example.txt")

# Delete file
if os.path.exists("copy_example.txt"):
    os.remove("copy_example.txt")
    print("File deleted")