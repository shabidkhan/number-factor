user=int(input('enter no. '))
list1=[]
i=1
while 1<user:
	if user %i==0:
		list1.append(i)
		user//=i
		i=2
		print(user)
	i+=1
print(list1)
