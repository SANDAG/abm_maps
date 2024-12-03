import os

# Define the root directory (your GitHub Pages root folder)
root_dir = './'

# Walk through all directories and subdirectories
for root, dirs, files in os.walk(root_dir):
    # Skip the root directory itself to avoid creating index.html at the root
    if root == root_dir:
        continue
    
    # Check if the directory contains files
    if files:
        # Define the index.html file path for the folder
        index_file_path = os.path.join(root, 'index.html')
        
        # Open the index.html file for writing
        with open(index_file_path, 'w') as f:
            f.write(f"<html><body><h1>Files in {root}</h1><ul>\n")
            for file in files:
                # Create a link for each file in the directory
                file_url = os.path.join(root.replace(root_dir, ''), file).replace(os.sep, '/')
                f.write(f'<li><a href="{file_url}">{file}</a></li>\n')
            f.write("</ul></body></html>\n")
