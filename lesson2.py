    #   0     1    2         3
ages = [10, "da", 10.1, [-190, 1, 1]]

ages.append(91)
age = 9

ages.extend([age])
# print(ages[3][0])
# print(ages)


nums = []

d = 0

while d < 5:
    num = int(input())
    nums.append(num)
    d = d + 1


print(nums)

d = 0

while d < 5:
    nums[d] = int(input())
    d = d + 1

print(nums)