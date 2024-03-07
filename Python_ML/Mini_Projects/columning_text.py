#TODO: need to change the parsing into a regex
text = """Print current directory path    #    pwd
List directories    #    ls
List directories including hidden    #    ls -a|--all
List directories in long form    #    ls -l
List directories in long form with human readable sizes    #    ls -l -h|--human-readable
List directories by modification time, newest first    #    ls -t
List size, created and modified timestamps for a file    #    stat foo.txt
List size, created and modified timestamps for a directory    #    stat foo
List directory and file tree    #    tree
List directory and file tree including hidden    #    tree -a
List directory tree    #    tree -d
Go to foo sub-directory    #    cd foo
Go to home directory    #    cd
Go to home directory    #    cd ~
Go to last directory    #    cd -
Go to foo sub-directory and add previous directory to stack    #    pushd foo
Go back to directory in stack saved by `pushd`    #    popd"""

# Define the file path where you want to save the text
file_path = input("Choose the file by entering its filepat ")
# replace # with $
symbolReplace = text.replace("#", "$")
# Split the text into lines
lines = symbolReplace.split('\n')
# Split each line into columns using the "#" delimiter and format the text
formatted_lines = [f"{lines.split('$')[0].strip():<50} $ {lines.split('$')[1].strip()}" for lines in lines]
# Open the file for writing and write the formatted text
if not file_path:
    with open(file_path, "w") as file:
        file.write("\n".join(formatted_lines))
else:
    with open(file_path, "a") as file:
        file.write("\n\n".join(formatted_lines))
    
print(f"Formatted text has been written to {file_path}")
