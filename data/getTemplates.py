




import os
import subprocess


languages = [ 'csharp','golang','java','javascript','ruby']
# Path to the directory which contains the folders
path_to_directory = "/Users/fhans/Documents/GenerativeBenchmarking/clone-anonymous-github/ChatGPT-Study-2757/data/problems"  # replace with your actual path

# Get a list of all folders in the directory
folder_names = [name for name in os.listdir(path_to_directory) if os.path.isdir(os.path.join(path_to_directory, name))]


# Loop over all folders
for folder_name in folder_names:


    # Change the current working directory
    os.chdir(os.path.join(path_to_directory, folder_name))
    
    # Loop over all languages
    for language in languages:
        

        # Your command line command
        command = f"leetcode show {folder_name} -g -l {language}"  # replace with your actual command

        # Execute the command
        process = subprocess.run(command, shell=True, check=True)

        

        # You may want to handle exceptions for the subprocess command.
        # For example, if the command isn't found or can't be executed, an exception will be raised.
        # You could catch the exception and print a meaningful error message instead.

