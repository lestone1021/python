def hello(greeting,*args):
	if (len(args)==0):
		print('%s!'%greeting)
	else:
		print('%s,%s!'%(greeting,','.join(args)))

hello('hi')
hello('hi','sarah')
hello('hello','michael','bob','adam')

names = ('bart','lisa')
hello('hello',*names)