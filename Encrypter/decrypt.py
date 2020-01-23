inp = list(input("encrypted message: "))
code = list(input("code: "))
num = []
for i in range(len(code)):
    num.append(code[i-1])
an = "abcdefghijklmnopqrstuvwxyz "
a1 = "mfwzojsidb qtgyhnckelrxpauv"
a2 = "nibmzhdfxakgstopeu wlvcryjq"
a3 = "rijzxemangpbdlvcyhwtkqfuso"
a4 = "iprfxkblzsdn otjhacmqyugvwe"
a5 = "mrsqldgyetnoixwpfzabkcuvjh"
a6 = "fmycxjdouirtla kwqenbhgsvpz"
a7 = "tjrdxaliemvpwqguo fybszkcnh"
a8 = "owaufgqxytrvznheplsikjdcbm"
a9 = "jzxdoiypcnvweutkra hfbqglsm"
a0 = "cvliohpb xgmrswfzneujqdatyk"
a = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
for n in num:

    for i in range(len(inp)):
        x = 0
        while inp[i] != a[int(n)][x]:
            x+=1
        inp[i] =an[x]
print(inp)