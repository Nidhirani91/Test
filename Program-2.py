a=int(input("Enter a number:"))
num_list=[]
for num in range(1,(a)*2):
	if (num%2)!=0:
		num_list.append(str(num))
print(','.join(num_list))



            
    