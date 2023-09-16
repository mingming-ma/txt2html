#!/usr/bin/env python3
import sys
import os
import shutil

def process_text_file(input_file, output_folder):
    # Read the input file, the input_file has path info
    filename = os.path.splitext(os.path.basename(input_file))[0]

    # Get each line of the input file
    try:
        with open(input_file, "r") as file:
            text_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        exit()

    # Combine each line with <p> tag
    bodyParagraph = ""
    for l in text_lines:
        updatedLine = l.strip()
        if(len(updatedLine)>1):
            bodyParagraph += "<p>" + updatedLine + "</p>\n"


    # Generate the HTML content
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{filename}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<!-- Generated content here... -->
{bodyParagraph}
</body>
</html>
"""

    # Write the HTML content to an output file
    output_file = os.path.join(output_folder, f"{filename}.html")

    try:
        with open(output_file, "w") as file:
            file.write(html_content)
        print(f"HTML file '{output_file}' generated successfully.")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

def process_folder(input_folder, output_folder):
    # Get all txt files in the input_folder, for now first depth, not recursive
    txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

    if not txt_files:
        print(f"No .txt files found in {input_folder}.")
        return
    
    for txt_file in txt_files:
        # Get the full path to the input .txt file
        input_file = os.path.join(input_folder, txt_file)
        process_text_file(input_file, output_folder)

def main():
    if len(sys.argv) < 2 or "-h" in sys.argv or "--help" in sys.argv:
        print("Usage:")
        print("   To generate html from a txt file: ./text2html.py input_file.txt")
        print("   To generate html from a folder which has txt files: ./text2html.py folder-name")
        sys.exit(0)
    elif "-v" in sys.argv or "--version" in sys.argv:
        print("Version: 0.1")
        sys.exit(0)

    # Create a folder named 'txt2html' or remove it if it exists
    output_folder = 'txt2html'
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    os.makedirs(output_folder)

    input_path = sys.argv[1]

    if os.path.isfile(input_path):
        process_text_file(input_path, output_folder)
    elif os.path.isdir(input_path):
        process_folder(input_path, output_folder)
    else:
        print("Error: Invalid input. Please provide a valid text file or folder.")

if (__name__ == "__main__"):
    main()