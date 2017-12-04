from random import randint
code = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(1,9))
message = list(input("what is your message? "))
print("this is your code: %s" %(code))
def encrypt(message,x):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r","s", "t", "u", "v", "w", "x", "y", "z", "a""a", "b", "c", "d", "e", "f", "g", "h","i","j", "k", "l", "m", "n", "o", "p", "q","r","s", "t", "u", "v", "w", "x", "y", "z", ]
	newMessage = []
	for index in message:
		n = 0
		if index != " ":
			while index != alphabet[n]:
				n = n + 1
			index = alphabet[n + int(x)]
		newMessage.append(index)
	return newMessage
for i in range(len(code)):
	message = encrypt(message,code[i])
message = ''.join(message)
print("your encrypted message is: %s" %(message))
input("")