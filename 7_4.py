def eval_loop():
	while True:
		line = raw_input('Please enter something to evaluate>>>')
		if line == 'done':
			break
		outpt = eval(line)
		print outpt
		
	return outpt
	
result = eval_loop()
print 'Exiting with final result:', result