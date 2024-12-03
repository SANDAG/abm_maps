import os

# Define the base directory (e.g., your repository root)
base_dir = "./"

exclude_folders = ['.github', '.git']

# Function to generate index.html for a given folder
def generate_index(dir_path):
    # Avoid generating index in any excluded folders
    if any(excluded in dir_path for excluded in exclude_folders):
        return
    
    files = os.listdir(dir_path)
    
    # Skip if the directory is empty
    if not files:
        return

    # Get the name of the directory for the heading
    dir_name = os.path.basename(dir_path)
    
    # Create index.html file
    index_content = f'<html><body><h1>Index of {dir_name}</h1><ul>'
    
    for file in files:
        file_path = os.path.join(dir_path, file)

        # Skip index.html from the listing
        if file == 'index.html':
            continue
        
        # Only include files (not directories) in the listing
        if os.path.isfile(file_path):
            file_url = file
            index_content += f'<li><a href="{file_url}">{file}</a></li>'
        elif os.path.isdir(file_path) and os.path.basename(file_path) != ".github":
            # Add directories, but avoid creating links for excluded directories like `.github`
            dir_url = file_path.replace(base_dir, "").replace(os.sep, "/")
            index_content += f'<li><a href="{dir_url}/">{file}/</a></li>'
    
    index_content += '</ul></body></html>'
    
    # Write the generated content to index.html in the folder
    with open(os.path.join(dir_path, 'index.html'), 'w') as index_file:
        index_file.write(index_content)

# Function to walk through directories and generate index files
def walk_directory(directory):
    # Iterate through the subdirectories and generate index files
    for dirpath, dirnames, filenames in os.walk(directory):
        # Avoid the .github folder and other unwanted folders
        if ".github" in dirpath:
            continue

        generate_index(dirpath)

# Call the function to walk the directory structure and generate index.html files
walk_directory(base_dir)
