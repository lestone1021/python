def ps(**kw):
	print('name  score')
	print('-----------')
	for name,score in kw.items():
		print('%10s %d' % (name,score))
	print()
	
ps(adam=99,lisa=88,bart=77)

data = {
	'adam':99,
	'lisa':88,
	'bart':77
}

ps(**data)

def pi(name,*,gen,city='beijing',age):
    print('Personal Info')
    print('-------------')
    print('Name:%s'%name)
    print('Gen: %s'%gen)
    print('City: %s'%city)
    print('Age: %s'%age)
    print()
    
pi('bob',gen='male',age=20)
pi('lisa',gen='female',city='shanghai',age=18)