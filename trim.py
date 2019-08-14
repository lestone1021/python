def trim(s):
	while s[:1]==' ':
		s=s[1:]
	while s[-1:]==' ':
		s=s[:-1]
	return s

if trim('hello ') != 'hello':
	print('失败!')
elif trim(' hello') != 'hello':
	print('失败!')
elif trim(' hello ') != 'hello':
	print('失败!')
elif trim(' hello world ') != 'hello world':
	print('失败!')
elif trim('   ') != '':
	print('失败!')
elif trim('') != '':
    print('失败!')
else:
	print('成功!')