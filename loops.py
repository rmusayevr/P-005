# a = 0
# while a < 10:
#     if a == 5:
#         a += 1
#         continue
#     elif a == 8:
#         break
#     print(a, '- while')
#     a += 1

# for a in range(0, 11, 3):
#     print(a)

# for b in range(11, 0, -2):
#     print(b)

# for c in range(-11, -4, 2):
#     print(c)

# for d in range(-4, -11, -2):
#     print(d)

# name = 'Elnur'

# for e in name:
#     print(e)

# print(len(name))
# string = ''
# for f in range(len(name)):
#     string += name[f]
#     print(string)

# number = int(input())
# count = 0
# while number > 0:
#     for i in str(number):
#         number -= int(i)
#     count += 1
# print(count)


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(a+b)
