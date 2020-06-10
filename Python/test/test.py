def push(val, result=[]):
	result.append(val)
	return result 

first = push(0)
push(1,first)
print(push(2))