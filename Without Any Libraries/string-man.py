str = input("Enter String:")
while True:
    ch = input("\n'1' to change the initial string \n'2' to copy string to another string\n'3' to concat string to another string\n'4' to find length of the string\n'5' to reverse the string\n'6' to exit\nEnter Choice")

    if ch == '1':
        str = input("\nEnter New String:")
        print(str,"\n")
        continue
    if ch == '2':
        cpy = str
        print("\nCopied String is", cpy)
    if ch == '3':
        con = input("\nEnter 2nd String:")
        print(str + " " + con)
    if ch == '4':
        count = 0
        for i in str:
            count += 1
        print('\nLength Of String = ', count)
    if ch == '5':
        count = 0
        for t in str:
            count += 1
        print('\nPrinting Reversed String....')
        t = count
        t -= 1
        rev = ''
        for i in range(count):
            rev = rev + str[t]
            t -= 1
        print(rev)
    if ch == '6':
        break
    else:
        continue
