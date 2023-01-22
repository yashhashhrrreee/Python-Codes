import os
def line_find():
        file = open('tsdl8.txt', 'r')
        line_total = -1   
        for line in file:
            if line != '\n':
                line_total += 1
        file.close()

        if line_total >= 1:
            print("\nTotal lines containing Text in file are = ",line_total)

        else:
            print("\nThe File is empty!")  
        
        return line_total

def spaces():
    file = open("tsdl8.txt", "r")
    count = 0
    while True:
        char = file.read(1)
        if char.isspace():
            count += 1
        if not char:
           break
    file.close()

    if count >= 1:
        print("\nNo of Spaces:: ",count)

    else:
        print("\nThe File is empty!")  
        

def word():
    file = open('tsdl8.txt', 'r')
    num_words = 0
    for line in file:
        words = line.split()
        num_words += len(words)

    file.close()

    if num_words >= 1:
        print("\nNo of Words :: ",num_words)

    else:
        print("\nThe File is empty!")  
        
    return num_words
line_find()
word()
spaces()

with open('tsdl8.txt') as infile:
    lines=0
    words=0
    characters=0
    for line in infile:
        wordslist=line.split()
        lines=lines+1
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)

print("\nNo of Characters::", characters)
                                                                                                                                    	

print("Finding the occurance of the given character")
while True:
    count = 0
    char = input('Enter Characters only: ')

    if not char.isalpha():
        print('Enter only letters')
        continue
    else:
        file =open('tsdl8.txt', 'r')
        for i in file:
            for c in i:
                if c == char:
                    count = count + 1
            print("The Character {} is found {} times  in the text file".format(char,count))
            break
	

