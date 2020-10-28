s = sum(i*i for i in range(10))                 # sum of squares
print(s, end='\n\n')

xvec = [10, 20, 30]
yvec = [7, 5, 3]
s = sum(x*y for x,y in zip(xvec, yvec))         # dot product
print(s, end='\n\n')

unique_words = set(word for line in 'pages'  for word in line.split())
print(unique_words, end='\n\n')

data = 'golf'
reverse = list(data[i] for i in range(len(data)-1, -1, -1))
print(reverse)