# 利用递归函数计算阶乘
# N!=1*2*3*4*5*6*……*N
def fa(n):
	if n ==1:
		return 1
	return fa(n-1)*n
	
print('fa(10)=',fa(10))

# 利用递归函数移动汉诺塔：
def move(n,a,b,c):
	if n == 1:
		print(a,'--',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(3,'A','B','C')
# 拆解
# move(3,a,b,c)=move(2,a,c,b);move(1,a,b,c);move(2,b,a,c)
# move(2,a,c,b)=move(1,a,b,c);move(1,a,c,b);move(1,c,a,b)
# move(2,b,a,c)=move(1,b,c,a);move(1,b,a,c);move(1,a,b,c)
# 故当n=3时
# A--C
# A--B
# C--B
# A--C
# B--A
# B--C
# A--C
# Over