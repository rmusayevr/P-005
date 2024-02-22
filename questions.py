# 7850
# n = int(input())
# l = list(map(int, input().split()))

# for i in l:
#     if l.count(i) < 2:
#         print(i, end=" ")


# 8961 
# n = int(input())
# l = list(map(int, input().split()))
# minimum = min(l)
# first = l[0]
# min_index = l.index(minimum)
# l.remove(first)
# l.remove(minimum)
# l.insert(0, minimum)
# l.insert(min_index, first)
# for i in l:
#     print(i, end=' ')


# 8965
# n = int(input())
# l = list(map(int, input().split()))
# minimum = int(min(l)/2)
# for i in l:
#     print(i-minimum, end = " ")

# 901

# count = 0
# a = input()
# for i in range(len(a)):
#     if i == 0 and (a[0] == "+" or a[0] == "-"):
#         pass
#     elif a[i] == "+" or a[i] == "-" or a[i] == "*":
#         count += 1
# print(count)

# 8696

# number = input()
# if number.count("2") > number.count("5"):
#     print(2)
# elif number.count("5") > number.count("2"):
#     print(5)
# else:
#     print("=")
    

# 8571
    
# sentence = input().upper()
# letter = input().upper()

# print(sentence.count(letter))


# 8981

# sentence = input()
# if sentence.count(" ") == 0:
#     print(-1)
# else:
#     last_index = 0
#     for i in range(len(sentence)):
#         if sentence[i] == " ":
#             last_index = i

#     print(sentence.index(" "), last_index)

# 8986 

# word = input()
# new_word = ""
# for i in word:
#     if i == "a":
#         new_word += "b"
#     elif i == "b":
#         new_word += "a"
#     else:
#         new_word += i
        
# print(new_word)

# s = input()
# s1 = s.replace("a", "1")
# s2 = s1.replace("b", "a")
# s3 = s2.replace("1", "b")
# print(s3)

# 8318

# n = input()
# n = n.replace('3', '')
# n = n.replace('9', '')
# print(n)





