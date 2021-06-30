import string
letter = str(input())

# upper = list(string.ascii_uppercase) 
# lower = list(string.ascii_lowercase)

# if letter in upper:
#     print(upper.index(letter)+65)
# elif letter in lower:
#     print(lower.index(letter)+97)
# elif int(letter) in range(0,10):
#     print(int(letter) + 48)

print(ord(letter))