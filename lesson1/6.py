arr = [120, 90, 312, 14, 5, 6, 7, 8,1233232,123233]
n = len(arr)
last_index = n - 1
# print(arr[last_index])
#8 [0,1,2,3,4,5,6,7]
for i in range(n):
    print(arr[i])

# print(arr[4])
# 120 90 312 14 5
#  0   1  2  3  4
#range -> генератор
#range(3) -> [0,1,2]
# for i in range(6):
#     print(i)
# for i in arr:
#     print(i)

for index, value in enumerate(arr):
    print(index,value)