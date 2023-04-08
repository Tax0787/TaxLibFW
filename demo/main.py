while 1:
	a=input('Looking Exam : ')
	match a:
		case 'Arcaives':
			import demo.ExamArcaives.main
		case 'exit':
			break
		case 'help':
			print('''
exit : exiting the ExamArcaives Information App
help : It's tell you help massage (prints this massage)
"Arcaives" Explanatory course items's Arcaive apps examples
''')
		case _:
			print(f'No Exam That {a}')