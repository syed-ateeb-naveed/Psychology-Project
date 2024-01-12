Categories=[0, 3, 12, 3, 6, 3, 12]
temp=[0, 3, 12, 3, 6, 3, 12]
categories=Categories.sort()
max_value = Categories[-1]
second_max_value = Categories[-2]
maxindex=temp.index(max_value)
second_max_index=temp.index(second_max_value)

print(maxindex,second_max_index)