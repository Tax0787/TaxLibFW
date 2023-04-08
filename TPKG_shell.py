from os import system as s
from os import chdir as c

a = lambda f: s(f'python {f}.py')
print('TPKG_shell is started')
while 1:
	b = input('>_')
	if b == 'file':
		a(input('file : '))
	elif b == 'exit':
		break
	elif b == 'help':
		print('''help : this
file : execution a file commands
exit : exiting
shells : execution terminal
demo : see you demo
        ''')
	elif b == 'demo':
		import demo.main
	elif b == 'shells':
		while 1:
			b = input('% ')
			if b == 'exit':
				break
			elif 'cd' in b:
				c(b.replace('cd ', ''))
			else:
				s(b)
	else:
		print(f"here are no command {b}\nso,you need 'help', right?")
input('TPKG_shell Is Finished')
