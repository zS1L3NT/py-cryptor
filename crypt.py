from string import ascii_lowercase as lwc
from string import ascii_uppercase as upc
dop = list("1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
kpp = list("klmnopqrstuvwxyzabcdefghij")

def altChar(char, change):
	if char in lwc:
		if lwc.index(char) + change > 25:
			return lwc[lwc.index(char) + change - 26]
		return lwc[lwc.index(char) + change]
	if char in upc:
		if upc.index(char) + change > 25:
			return upc[upc.index(char) + change - 26]
		return upc[upc.index(char) + change]
	if char.isdigit():
		if int(char) + change > 9: return str(int(char) + change - 10)
		elif int(char) + change < 0: return str(int(char) + change + 10)
		return str(int(char) + change)
	return char

def altCase(char):
	if char in lwc:
		return upc[lwc.index(char)]
	elif char in upc:
		return lwc[upc.index(char)]
	return char

def encrypt(string):
	tmp = list(string)
	res = ''
	popped = False
	if len(tmp) % 2 == 1: tmp.pop(); popped = True
	for i in range(0, len(tmp), 2): res += tmp[i + 1] + tmp[i]
	res += string[-1] if popped else ''
	###
	tmp = list(res)
	res = ''
	for i in range(0, len(tmp)):
		kppi = i
		while kppi > 25: kppi -= 26
		res += kpp[kppi] + tmp[i]
	###
	tmp = list(res)
	res = ''
	for i in range(0, len(tmp)):
		if i % 4 == 0 or i % 4 == 3: res += altChar(tmp[i], 1)
		elif i % 4 == 1 or i % 4 == 2: res += altChar(tmp[i], -1)
	###
	tmp = list(res)
	res = ''
	for i in range(len(tmp), 0, -1): res += tmp[i - 1]
	###
	tmp = list(res)
	for i in range(1, len(tmp), 2): tmp[i] = altCase(tmp[i])
	###
	res = ''
	for i in range(0, len(tmp)):
		if i % 4 == 0: res += altChar(tmp[i], 3)
		elif i % 4 == 1: res += altChar(tmp[i], -6)
		elif i % 4 == 2: res += altChar(tmp[i], -3)
		elif i % 4 == 3: res += altChar(tmp[i], 2)
	###
	tmp = list(res)
	res = ''
	for i in range(0, len(tmp)):
		dopi = i
		while dopi >= 100: dopi -= 100
		res += tmp[i] + dop[dopi]
	return res

def decrypt(string):
	res = ''
	for i in range(1, len(string), 2):
		if string[i] != dop[int(i / 2)]: return 'Invalid code entered!'
	for i in range(0, len(string), 2): res += string[i]
	###
	tmp = list(res)
	res = ''
	for i in range(0, len(tmp)):
		if i % 4 == 0: res += altChar(tmp[i], -3)
		elif i % 4 == 1: res += altChar(tmp[i], 6)
		elif i % 4 == 2: res += altChar(tmp[i], 3)
		elif i % 4 == 3: res += altChar(tmp[i], -2)
	###
	tmp = list(res)
	for i in range(1, len(tmp), 2): tmp[i] = altCase(tmp[i])
	###
	res = ''
	for i in range(len(tmp), 0, -1): res += tmp[i - 1]
	###
	tmp = list(res)
	res = ''
	for i in range(0, len(tmp)):
		if i % 4 == 0 or i % 4 == 3: res += altChar(tmp[i], -1)
		elif i % 4 == 1 or i % 4 == 2: res += altChar(tmp[i], 1)
	###
	tmp = list(res)
	res = ''
	for i in range(0, len(tmp), 2):
		if tmp[i] != kpp[int(i / 2)]: return 'Invalid code entered!'
	for i in range(1, len(tmp), 2): res += tmp[i]
	###
	tmp = list(res)
	res = ''
	popped = False
	if len(tmp) % 2 == 1: popped = tmp[-1]; tmp.pop()
	for i in range(0, len(tmp), 2): res += tmp[i + 1] + tmp[i]
	res += popped if popped else ''
	return res

print('Python Custom Encryptor')
extra = ''
e = ['e', 'E']
d = ['d', 'D']
while not extra:
	mode = str(input('Encrypt(e) or Decrypt(d): '))
	if mode in e:
		extra = 'En'
	elif mode in d:
		extra = 'De'
	else:
		print('Invalid encryption type!\n')

message = str(input('Enter message to ' + extra + 'crypt: '))

print(extra + 'crypted message:')

resp = ''
broken = message.split()
if len(broken) == 1: print('\t' + (encrypt(message) if mode in e else decrypt(message)))
else:
	for i in range(0, len(broken)):
		resp += (encrypt(broken[i]) if mode in e else decrypt(broken[i])) + " "
	print('\t' + resp.strip())


# After 2 months of coding JavaScript and gaining
# more experience, I cut down my Python cryptor's
# number of lines of code from
# 670 lines of code in 3 files to
# 127 lines of code in 1 file