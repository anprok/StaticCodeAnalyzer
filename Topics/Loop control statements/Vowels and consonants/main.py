vowels = list('aeiou')
non_alphabet = list(" !,./")
sequence = input()
for symbol in sequence:
    if symbol in non_alphabet:
        break
    if symbol in vowels:
        print("vowel")
    else:
        print("consonant")