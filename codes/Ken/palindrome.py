def is_pal(word):
    word = word.lower()
    if len(word) > 1:
        for i in range(len(word)):
            if word[i] == word[-1*(i+1)]:
                if i == len(word) - 1:
                    return True
                else:
                    continue
            else:
                return False

def reverse(word):
    word = word.lower()
    if len(word) > 1 and is_pal(word) == False:
        rev_word = ""
        for i in range(len(word)):
            rev_word += word[-1*(i+1)]
        return rev_word

words = []
while True:
    word = input("Enter a word: ")
    if word == "exit" or word == "Exit" or word == "EXIT" or word =="q":
        print("The palindromes you entered are: ", words)
        print("See you next time! :)")
        break  
    word = word.strip()
    is_palindrome = is_pal(word)
    if is_palindrome == True:
        print(f"{word} is a palindrome") 
        words.append(word)       
    else:
        print(f"{word} is not a palindrome. The reverse of {word} is {reverse(word)}")
             

    