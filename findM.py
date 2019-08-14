def find(L):
	if not L:
		return(None,None)
	for n in L:
		return(min(L),max(L))

if find([]) != (None,None):
    print('测试失败!')
elif find([7]) != (7, 7):
    print('测试失败!')
elif find([7, 1]) != (1, 7):
    print('测试失败!')
elif find([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')