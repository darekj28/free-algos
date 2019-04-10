
N = 20

# a is a list of size N
a = [range(0, N)]

# linear run time example

max_element = a[0]
for i in range(0, N):
	max_element = max(a[i], max_element)



# quadratic run time example

count = 0
for i in range(0, N):
	for j in range(i+1, N):
		if a[i] + a[j] == 0:
			count += 1

# cubic run time example

count = 0
for i in range(0, N):
	for j in range(i+1, N):
		for k in range(j+1,N):
			if a[i] + a[j] + a[k] == 0:
				count += 1






 