# score = int(input())

# if 51 <= score <= 60:
#     print("E")
# elif 61 <= score < 71:
#     print("D")
# elif score >= 71 and score <= 80:
#     print("C")
# elif 81 <= score <= 90:
#     print("B")
# elif 91 <= score <= 100:
#     print("A")
# elif 0 <= score <= 50:
#     print("F")
# elif score < 0 or score > 100:
#     print("Zəhmət olmasa, düzgün ədəd daxil edin (0-100 arasında)")


# name = input("Enter your name: ")
# if name != "John":
#     print("Your name is not John")
# else:
#     print(f"Your name is {name}")

# age = int(input("How old are you? "))

# if age > 18:
#     if age % 2 == 0:
#         print("Sənin yaşın 18'dən çoxdur və 2'ə tam bölünür")
#     elif age % 2 == 1:
#         print("Sənin yaşın 18'dən çoxdur və 2'ə tam bölünmür")

# x = int(input())

# if x < 5:
#     y = x**2 - 3*x + 4
#     print(y)
# elif x >= 5:
#     print(x+7)

# x, y = map(int, input().split())
# if x > y:
#     print(y, x)
# elif x <= y:
#     print(x, y)

x, a, b = map(int, input().split())

if (a <= x <= b):
    print("YES")
else:
    print("NO")



