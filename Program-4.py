def count_dict(arr):
    count={}
    for i in arr:
        count[i] = count.get(i, 0) + 1
    return count

arr=[1,2,8,9,12,46,76,82,15,20,30]
print(count_dict(arr))
