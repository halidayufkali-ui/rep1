import os

# Create directory
os.mkdir("test_dir")

# Create nested directories
os.makedirs("parent/child", exist_ok=True)

# List directories
print("List of files and folders:")
print(os.listdir("."))

# Current working directory
print("Current directory:", os.getcwd())