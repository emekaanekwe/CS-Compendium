from pathlib import Path
import sys

def print_tree(path: Path, write_func, prefix: str = '', show_files: bool = True):
    """Recursively prints the directory tree structure using the provided write function."""
    if prefix == '':
        write_func(f"{path.name}/")
    
    # Get all entries, sort them (dirs first, then files, alphabetically) using lambda
    entries = dict(sorted({entry: entry.name.lower() for entry in path.iterdir()}.items(), key=lambda x: (x[0].is_file(), x[1])))

    
    # Determine the connector and the new prefix for each entry
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        
        if entry.is_dir():
            write_func(f"{prefix}{connector}{entry.name}/")
            # Recurse into subdirectory
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(entry, write_func, new_prefix, show_files)
        elif show_files:
            write_func(f"{prefix}{connector}{entry.name}")

def output_tree(path: Path, output_mode: str = 'console', file_path: str = None, show_files: bool = True):
    """
    Output directory tree to console, file, or both.
    
    Args:
        path: Path to the directory
        output_mode: 'console', 'file', or 'both'
        file_path: Path to output file (required if output_mode includes 'file')
        show_files: Whether to show files in the tree
    """
    if output_mode not in ['console', 'file', 'both']:
        raise ValueError("output_mode must be 'console', 'file', or 'both'")
    
    if output_mode in ['file', 'both'] and file_path is None:
        raise ValueError("file_path must be provided when output_mode is 'file' or 'both'")
    
    write_funcs = []
    if output_mode in ['console', 'both']:
        write_funcs.append(lambda s: print(s))
    if output_mode in ['file', 'both']:
        f = open(file_path, 'w')
        write_funcs.append(lambda s: f.write(s + '\n'))
    
    def combined_write(s):
        for wf in write_funcs:
            wf(s)
    
    try:
        print_tree(path, combined_write, show_files=show_files)
    finally:
        if 'f' in locals():
            f.close()

# Example usage
start_path = Path('insert path here')

# Output to console only
#output_tree(start_path, output_mode='console')

# Output to file only
#output_tree(start_path, output_mode='file', file_path='directory_tree.txt')

# Output to both
# output_tree(start_path, output_mode='both', file_path='directory_tree.txt')
