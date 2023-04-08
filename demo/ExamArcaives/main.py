while 1:
	a=input('Looking Exam : ')
	match a:
		case 'introduction':
			import demo.ExamArcaives.introduction_app
		case 'exit':
			break
		case 'help':
			print('''
exit : exiting the ExamArcaives Information App
help : It's tell you help massage (prints this massage)
"introduction" Explanatory course items's apps
''')
		case _:
			print(f'No Exam That {a}')