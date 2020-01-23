inp = list(input("message: ")) 
num = str(input("code: "))
an = "abcdefghijklmnopqrstuvwxyz "
a1 = "mfwzojsidb qtgyhnckelrxpauv"
a2 = "nibmzhdfxakgstopeu wlvcryjq"
a3 = "rijzxemangpbdlvcyhwtkqfu so"
a4 = "iprfxkblzsdn otjhacmqyugvwe"
a5 = "mrsqldgyetnoixwpfzabkcuv jh"
a6 = "fmycxjdouirtla kwqenbhgsvpz"
a7 = "tjrdxaliemvpwqguo fybszkcnh"
a8 = "owau fgqxytrvznheplsikjdcbm"
a9 = "jzxdoiypcnvweutkra hfbqglsm"
a0 = "cvliohpb xgmrswfzneujqdatyk"
for n in num:
	for i in range(len(inp)):
		x = 0
		while inp[i] != an[x]:
			x += 1
		if int(n) == 1:
			inp[i] = a1[x]
		if int(n) == 2:
			inp[i] = a2[x]
		if int(n) == 3:
			inp[i] = a3[x]
		if int(n) == 4:
			inp[i] = a4[x]
		if int(n) == 5:
			inp[i] = a5[x]
		if int(n) == 6:
			inp[i] = a6[x]
		if int(n) == 7:
			inp[i] = a7[x]
		if int(n) == 8:
			inp[i] = a8[x]
		if int(n) == 9:
			np[i] = a9[x]
		if int(n) == 0:
			inp[i] = a0[x]
	print(inp)
	
print(''.join(inp))

