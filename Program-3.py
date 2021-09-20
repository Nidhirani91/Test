def generate_seq(num):
    num_list = []
    if num % 2 == 0:
        num -= 1
    for i in range(1, (num)*2):
        if (i % 2) != 0:
            num_list.append(str(i))
    return ','.join(num_list)
num=int(input("Enter a number:"))
print(generate_seq(num))
