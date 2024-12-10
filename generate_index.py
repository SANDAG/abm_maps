import os

# Define the base directory (e.g., your repository root)
base_dir = "./"

exclude_folders = ['.github', '.git']

# Function to generate index.html for a given folder
def generate_index(dir_path):
    # Avoid generating index in any excluded folders
    if any(excluded in dir_path for excluded in exclude_folders):
        return
        
    files = sorted(os.listdir(dir_path))

    # Get the name of the directory for the heading
    dir_name = os.path.basename(dir_path)

    # Create index.html file with a heading and a "Go to Parent Directory" link
    index_content = f'<html><body>'

    # Add a link to go to the parent directory
    parent_dir_url = os.path.dirname(dir_path).replace(base_dir, "").replace(os.sep, "/")
    if parent_dir_url != "":
        index_content += f'<p><a href="../">.. (Parent Directory)</a></p>'
    
    if dir_path != base_dir:
        index_content += '<p>Destination MGRA in red; MGRA or TAZ w access in blue.</p>'
    # Add the heading for the current directory
    index_content += f'<h1>Index of {dir_name}</h1><ul>'

    # Track if there are any valid files or directories to list
    has_content = False
    
    for file in files:
        file_path = os.path.join(dir_path, file)

        # Skip index.html from the listing
        if file == 'index.html':
            continue
        
        # Only include files (not directories) in the listing
        if os.path.isfile(file_path) and file.endswith('.html'):
            file_url = file
            index_content += f'<li><a href="{file_url}">{file}</a></li>'
            has_content = True
        elif os.path.isdir(file_path) and os.path.basename(file_path) != ".github":
            # Add directories, but avoid creating links for excluded directories like `.github`
            dir_url = file_path.replace(base_dir, "").replace(os.sep, "/")
            index_content += f'<li><a href="{dir_url}/">{file}/</a></li>'
            has_content = True
    # If no valid files or directories were found, still create the index file with a message
    if not has_content:
        index_content += '<li>No files or directories to display.</li>'
    
    index_content += '</ul></body></html>'
    
    # Write the generated content to index.html in the folder
    try:
        with open(os.path.join(dir_path, 'index.html'), 'w') as index_file:
            index_file.write(index_content)
    except Exception as e:
        print(f"Error writing index.html in {dir_path}: {e}")

# Function to walk through directories and generate index files
def walk_directory(directory):
    # Iterate through the subdirectories and generate index files
    for dirpath, dirnames, filenames in os.walk(directory):
        # Avoid the .github folder and other unwanted folders
        if any(excluded in dirpath for excluded in exclude_folders):
            continue

        generate_index(dirpath)

# Call the function to walk the directory structure and generate index.html files
walk_directory(base_dir)
