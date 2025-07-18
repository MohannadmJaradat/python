char = input("Please enter a character: ")
while char!="-1":
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")
    char = input("Please enter a character: ")