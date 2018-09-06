# Gudni Natan Gunnarsson
# 5.9.2018
# Forritun

string = input("Enter a sentence: ")

lower = 0
upper = 0
decimal = 0
punctuation = 0

for c in string:
    if c.islower():
        lower += 1
    elif c.isupper():
        upper += 1
    elif c.isdecimal():
        decimal += 1
    elif c.isspace() == False:
        punctuation += 1

print('{:>15} {:>5}'.format("Upper case", upper))
print('{:>15} {:>5}'.format("Lower case", lower))
print('{:>15} {:>5}'.format("Digits", decimal))
print('{:>15} {:>5}'.format("Punctuation", punctuation))