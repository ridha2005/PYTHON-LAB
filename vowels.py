word = input("Enter a word: ")
vowels =['a','e','i','o','u','A','E','T','O',]
vowel_list=[]
for ch in word:
     if ch in vowels:
        vowel_list.append(ch)
print("Vowels:",vowel_list)