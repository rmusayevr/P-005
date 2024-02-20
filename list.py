# positive_numbers = [2, 39, 18, 102, 48, 754]
# empty_list = [] or list()
# negative_numbers = list([-2, -239, -585, -38])
# numbers = [2, 39, 18, 102, 48, 754, -2, -239, -585, -38, 2]

# for i in range(len(positive_numbers)):
#     print(positive_numbers[i], ' - number')
#     print(i, ' - index')

# a = list(map(int, input()))
# print(a[::-1])
# for i in a[::-1]:
#     print("".join(str(i)), end="")

# print(positive_numbers[2:4])
# print(negative_numbers[::-1])
# print(numbers[1:8:4])


# print(sorted(numbers))
# print(list(reversed(numbers)))
# print(numbers.count(2))
# numbers.append(19)
# print(numbers)
# numbers.clear()
# print(numbers)
# new_list = numbers.copy()
# new_list.append(29)
# numbers.pop()
# print(new_list)
# print(numbers)
# print(numbers.index(2))
# numbers.extend([220, 14, 5])
# numbers.insert(1, 10)
# numbers.remove(48)
# print(numbers)

# l = [1, 1]
# n = int(input())
# for i in range(2, n+1):
#     a = l[i-2] + l[i-1]
#     l.append(a)
# print(l[-1])

# n = int(input())
# a = list(map(int, input().split()))
# count = 0
# for i in range(1, n-1):
#     if a[i] > a[i-1] and a[i] > a[i+1]:
#         count += 1
# print(count)

# number = str(input())
# for i in range(len(number)):
#     digit = int(number[i])
#     if digit % 2 != 0:
#         digit -= 1
#     else:
#         digit += 1
#     print(digit, end="")


n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    if a.count(a[i]) < 2:
        print(a[i], end=" ")

