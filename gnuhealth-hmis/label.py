import os
import sys
import argparse

parser = argparse.ArgumentParser(description="""
A script to add hierarchical labels to headers in .rst files based on a predefined hierarchy of header underline strings. The script processes .rst files in the specified directory and its subdirectories to find headers and add hierarchical labels to them. These labels are constructed using the file path and header text, facilitating easy referencing in documentation.\n 

A label is constructed as follows:
- It starts with ".. _" followed by the file name (with path separators replaced by '-' and '.rst' extension removed).
- Next, the texts of all parent headers (replacing spaces with '_') are added, separated by '-'.
- The label ends with ":\\n".
- This full label is inserted above the respective header line in the .rst file.

For example, for a header in file "docs/subdir/file.rst" with text "My Header" and no parent headers, the label will be ".. _docs-subdir-file:my_header:\\n".
""", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("path", help='Path to the project directory containing .rst files.\nThe script will recursively walk through this directory to find and modify .rst files.')

args = parser.parse_args()
path = args.path

def add_hierarchical_labels(base_path):
    # Hierarchy of header delimiter strings
    hierarchy = ['===', '---', '^^', '""']

    # Walk through all files in the given path recursively
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                
                new_lines = []
                i = 0
                stack = []  # Stack to store the current hierarchical headers
                while i < len(lines):
                    line = lines[i]

                    # Check if the current line is a header
                    current_hierarchy = None
                    for h in hierarchy:
                        if i + 1 < len(lines) and lines[i + 1].startswith(h):
                            current_hierarchy = h
                            break

                    if current_hierarchy:
                        while stack and hierarchy.index(stack[-1][1]) >= hierarchy.index(current_hierarchy):
                            stack.pop()
                        
                        header_name = line.strip().replace(' ', '_').lower()
                        stack.append((header_name, current_hierarchy))

                        label_name = os.path.relpath(file_path, base_path).replace(os.sep, '-').replace('.rst', '')
                        full_label = "-".join([item[0] for item in stack])
                        label = f".. _{label_name}:{full_label}:\n\n"
                        
                        # If the previous line is a false formated label, skip it
                        if new_lines and new_lines[-1].startswith(".. _"):
                            new_lines.pop()

                        # If the there exists already a label skip it
                        if new_lines and new_lines[-2].startswith(".. _") and new_lines[-1].startswith("\n"):
                            new_lines.pop()
                            new_lines.pop()

                        new_lines.append(label)
                    
                    new_lines.append(line)
                    i += 1
                
                # Write the updated lines back into the file
                with open(file_path, 'w') as f:
                    f.writelines(new_lines)

if not os.path.exists(path):
    print(path + ' does not exist', file=sys.stderr)
else:
    add_hierarchical_labels(path)