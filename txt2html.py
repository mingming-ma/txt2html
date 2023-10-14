#!/usr/bin/env python3
import sys
import os
import shutil
import argparse
import re
import tomli

# # TO-DO #1: implement contains_bold(word)
# def contains_bold(word):
#     # Define regex pattern for bold syntax (asterisk)

#     # Define regex pattern for bold syntax (underscore)

#     # Return true if word matches either RegEx pattern, False otherwise using re.search(regex, string)

def contains_italics(word):
    # Markdown Pattern Regular Expressions

    # Matches *word*, *WORD*, *woRd*, **word**
    italic_pattern1 = r'(?<!\*)\*(?:\*|[^*]+)\*(?!\*)'

    # Matches _word_, _WORD_, _woRd_, __word__
    italic_pattern2 = r'(?<!\_)_(?:\_|[^*]+)_(?!\_)'

    # Return True if word matches either RegEx pattern, False otherwise
    return (re.search(italic_pattern1, word) or re.search(italic_pattern2, word))

def process_line(file_line):


    # Split updatedLine into words
    words = file_line.split()

    # Temporary line
    modifiedLine = ""
    for word in words:
        # This if/else structure checks if the word matches a Markdown regex pattern (italics only for now)
        # If the word matches a Markdown regex it is modified with appropriate HTML tags

        # Check if word matches either bold regex pattern:

        # # TO-DO #3: Uncomment lines 43-44 after completing TO-DO #2
        # if contains_bold(word):
            # # TO-DO #2: replace wrapper **...** or __...__ with <b>...</b> 
        # # TO-DO #4: Change line 48 to: elif contains_italics(word):

        # Check if word matches either italic regex pattern
        if contains_italics(word):
            # Replace beginning and ending '*' or "_" with <i>...</i> tags
            # Examples: 
            #   *word* -> <i>word</i>
            #   _word_ -> <i>word</i>
            #   _word* -> _word*
            #   __word__ -> <i>_word_</i> (note: this is an undesired conversion that will
            # be eliminated if you check for bold syntax before checking for italics syntax)
            word = '<i>' + word[1:-1] + '</i>'
        
        # At the end, add word to modifiedLine whether it was modified or not
        modifiedLine += word + ' '

    return modifiedLine

def process_text_file(input_file, output_folder, lang_attribute_value = "en-CA"):
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
    title = filename
    html_title = False



    # Read the first line
    if len(text_lines) >= 1:
        first_line = text_lines[0].strip()

        # Check if it's not empty and there are at least two more lines available
        if first_line and len(text_lines) >= 3 and text_lines[1].strip() == "" and text_lines[2].strip() == "":
            # Use first_line as a title content
            title = first_line
            bodyParagraph += f"<h1 lang=\"{lang_attribute_value}\">" + title + "</h1>"
            html_title = True

            for i in range(1, len(text_lines)):
                updatedLine = text_lines[i].strip()

                #Check if input_file is Markdown (.md)
                if (input_file.endswith(".md")):
                    if (updatedLine.__eq__("---")):
                        bodyParagraph += "<hr>"
                        continue
                    else:
                        # Process updatedLine with addition Markdown conversion logic
                        updatedLine = process_line(updatedLine)

                bodyParagraph += f"<p lang=\"{lang_attribute_value}\">"  + updatedLine + "</p>\n"

    if not html_title:
        for l in text_lines:
            updatedLine = l.strip()

            #Check if input_file is Markdown (.md)
            if (input_file.endswith(".md")):
                if (updatedLine.__eq__("---")):
                    bodyParagraph += "<hr>"
                    continue
                else:
                    # Process updatedLine with addition Markdown conversion logic
                    updatedLine = process_line(updatedLine)
                 
            bodyParagraph += f"<p lang=\"{lang_attribute_value}\">"  + updatedLine + "</p>\n"

    # Generate the HTML content
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
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

def process_folder(input_folder, output_folder, lang_attribute_value):
    # Get all target files in the input_folder, for now first depth, not recursive
    target_files = [f for f in os.listdir(input_folder) if (f.endswith(".txt") or f.endswith(".md"))]

    # Stop program if no .txt or .md files found in input_folder
    if not target_files:
        print(f"No .txt or .md files found in {input_folder}.")
        return
    
    for file in target_files:
        # Get the full path to the input .txt or .md file
        input_file = os.path.join(input_folder, file)
        process_text_file(input_file, output_folder, lang_attribute_value)

def main():
    version = "0.1.5"

    parser = argparse.ArgumentParser(description='txt2html')
    parser.add_argument('-o', '--output', help='Specify the output directory. Existing output folder will first be removed. If not specified, "./txt2html" will be used.')
    parser.add_argument('-v', '--version', action="version", version=f'txt2html {version}' ,help='Show the version')
    parser.add_argument('-l', '--lang', help='Specify the language to use when generating the lang attribute on the root <html> element. If not specified, "en-CA" will be used.')
    parser.add_argument ('-c', '--config', help="URL to a TOML config file to be used as a config for the HTML files")
    args, remaining_args = parser.parse_known_args()
    if (len(remaining_args) == 0):
        parser.error('Input is required. Use -h or --help for usage information.')

    input_path = remaining_args[0]

    # Use a folder name 'txt2html' under tool's folder as a default output folder
    output_folder = os.path.abspath('txt2html')

    if args.output:
        output_folder = os.path.abspath(args.output)

    lang_attribute_value = "en-CA"
    if args.lang:
        lang_attribute_value = args.lang

    if args.config:
        config_file_path = args.config
        try:
            with open(config_file_path, "rb") as config_file:
                config_data = tomli.load(config_file)
                
                output_folder = config_data.get("output", output_folder)
                lang_attribute_value = config_data.get("lang", lang_attribute_value)
        except FileNotFoundError:
            parser.error(f"Config file not found: {config_file_path}")
        except tomli.TOMLDecodeError:
            parser.error(f"Error parsing the config file: {config_file_path}")

    current_script_path = os.path.abspath(__file__)
    current_script_directory = os.path.dirname(current_script_path)

    #remove the output folder if it exists, except the directory containing the currently running script, or same as input folder
    if os.path.exists(output_folder):
        if current_script_directory == output_folder :
            parser.error("Can not override tool's folder")
        elif os.path.isdir(input_path) and os.path.abspath(input_path) == os.path.abspath(output_folder):
            parser.error("Can not override input folder")
        else:
            shutil.rmtree(output_folder)

    os.makedirs(output_folder)

    if os.path.isfile(input_path):
        process_text_file(input_path, output_folder, lang_attribute_value)
    elif os.path.isdir(input_path):
        process_folder(input_path, output_folder, lang_attribute_value)
    else:
        parser.error("Invalid input. Please provide a valid text file or folder.")

if (__name__ == "__main__"):
    main()