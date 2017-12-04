message = list(input("what is your message? "))
code = list(input("what is your code? "))
def decrypt(message,x):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r","s", "t", "u", "v", "w", "x", "y", "z", "a""a", "b", "c", "d", "e", "f", "g", "h","i","j", "k", "l", "m", "n", "o", "p", "q","r","s", "t", "u", "v", "w", "x", "y", "z", ]
	newMessage = []
	for index in message:
		n = 0
		if index != " ":
			while index != alphabet[n]:
				n = n + 1
			index = alphabet[n - int(x)]
		newMessage.append(index)
	return newMessage
for i in range(len(code)):
	message = decrypt(message, code[i])
message = ''.join(message)
print("your decrypted message is: %s" %(message))
input("")