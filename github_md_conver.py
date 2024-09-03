# Obsidian -> GitHub markdown Converter
# Author: HackerTyperAbuser
# Version: 1
# Date Started: 3/9/2024

# ASCII art ObsiGit IMG Converter

# TO DO:
# Optimize the code (function find_img() could be merge with update_file()?)
# Add caption procedure
# Add some ASCII art

# Using command line argument
import argparse
# Regex pattern
import re
import sys

parser = argparse.ArgumentParser(description="Python program that automates Obsidian image markdown text to Github markdown format")
# Main
def main():
    # Ask for file
    filename = str(input("File: "))
    # call function to excute operation this will return new text file.
    if convert(filename) == 0:
        print("[+] Write is complete")
        sys.exit()
    else:
        print("[!] Update function failed")
        sys.exit()
   
# Function to call all 
def convert(filename):
    array_match = find_img(filename, array_match = [])
    array_encoded = url_encode(array_match, array_encoded= [])
    update_file(filename, array_encoded)
    return 0
# Open a file(file)
def find_img(filename , array_match):
    # array containing the string with the pattern (obisidan img tag)
    # exception for opening a file
    try:
        # Open the file and read line by line
        with open(filename, 'r') as file:
            # enumerate, line number, and line
            for line_number, line in enumerate(file, start=1):
                # Find the first one with "![[...]]" given this pattern
                pattern = r'!\[\[.*?\]\]'
                # matches is an arry that has the string
                matches = re.findall(pattern, line)
                # append the different match to an array
                if matches:
                    for match in matches:
                        array_match.append(match)
        file.close()
        return array_match
            # url_encode(array_match)
    except FileNotFoundError:
        print(f"[!] {filename} does not exist")
        sys.exit()

# String converter(get string)
def url_encode(array_match, array_encoded):

    # Convert to URL encoded format
    for match in array_match:
        # replace " " with %20 for url encoded format
        encoded_match = match.replace(" ", "%20")
        # get only the string to add to the div element
        pattern = r'!\[\[(.*?)\]\]'
        match = re.search(pattern, encoded_match)
        if match:
            result = match.group(1)
            array_encoded.append(result)
    # return formatted string with div
    array_div_extend = div_add(array_encoded, array_div_extend=[])
    return array_div_extend

# div_add(![[Pasted%20image%2020240830195100.png]], return value from string converter)
def div_add(array_encoded, array_div_extend):
    # Change the entire string to 
    div_template = '''\n<div align="center">\n\t<img src="img/{encoded_match}">\n</div>\n'''
    # append the return value from string converter to the image tag
    for encoded_match in array_encoded:
        str_with_div = div_template.format(encoded_match=encoded_match) 
        array_div_extend.append(str_with_div)

    return array_div_extend

# Write update file
def update_file(filename, array_encoded):
    
    # User input for destination of updated file
    path_dest = str(input("PATH: "))
    destination = f"{path_dest}"

    print("[+] New file created!")
    # Find the string with the pattern again
    with open(filename, 'r') as source, open(destination, 'w') as dest:
        count = 0
        for line in source:
            pattern = r'!\[\[.*?\]\]'
            matches = re.findall(pattern, line)
            if matches:
                for match in matches:
                    if count < len(array_encoded):
                        line = line.replace(match, array_encoded[count], 1)
                        count += 1
            # Write the modified line
            dest.write(line)
    source.close()
    dest.close()
    return 0
                    
# add_cap(fig_count)
def add_cap():
    pass
    # What is the caption for this figure?
    # add the line <p><em>User input</em></p> to the file

if __name__ == "__main__":
    main()