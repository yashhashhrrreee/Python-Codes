import re

def file_stats(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    characters = 0
    words = 0
    spaces = 0
    non_blank_lines = 0
    special_characters = 0
    for line in lines:
        if line.strip() == "":  # skip blank lines
            continue
        non_blank_lines += 1
        wordslist = line.strip().split(" ")
        words += len(wordslist)
        characters += len(line)
        spaces += line.count(" ")
        special_characters += len(re.findall('[^a-zA-Z0-9\n\r\t ]', line))
    return characters, words, spaces, non_blank_lines, special_characters

file_path = "file.txt"
characters, words, spaces, non_blank_lines, special_characters = file_stats(file_path)
print("Characters:", characters)
print("Words:", words)
print("Spaces:", spaces)
print("Lines:", non_blank_lines)
print("Special Characters:", special_characters)
