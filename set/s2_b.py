frontend = {'html', 'css', 'java', 'javascript', 'bootstrap'}
backend = {'javascript', 'java', 'python', 'golang', 'dodnet'}

frontend = list(frontend)
frontend.insert(1, 'sass')
frontend = set(frontend)
print(frontend)
