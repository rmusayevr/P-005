python_dict = {
    "name": "Python",
    "year": 1991,
    "founder": "Guido van Rossum",
    "extension": "py",
    "version": 3.12,
}

# pascal_dict = dict(name="Pascal", year=1970, founder="Niklaus Wirth", extension="pas", version=3.2)

# print(type(python_dict))
# print(python_dict)
# print(type(pascal_dict))
# print(pascal_dict)
# print("*"*60)
# print("The name of the programming language:", python_dict['name'])
# print("The year of the programming language:", python_dict['year'])
# print("The founder of the programming language:", python_dict['founder'])
# print("The extension of the programming language:", python_dict['extension'])
# print("The version of the programming language:", python_dict['version'])
# print("*"*60)
# print("The name of the programming language:", pascal_dict.get('name'))
# print("The year of the programming language:", pascal_dict.get('year'))
# print("The founder of the programming language:", pascal_dict.get('founder'))
# print("The extension of the programming language:", pascal_dict.get('extension'))
# print("The version of the programming language:", pascal_dict.get('version'))
# print("*"*60)


# print(python_dict.keys())
# print(type(python_dict.keys()))
# print(python_dict.values())
# print(type(python_dict.values()))
# print(python_dict.items())
# print(type(python_dict.items()))

# for keys, values in python_dict.items():
#     print(keys, ":", values)

# for i in python_dict:
#     print(str(i) + ": " + str(python_dict[i]))

# for i in pascal_dict.values():
#     print(i)

# for i in pascal_dict.keys():
#     print(str(i) + ": " + str(pascal_dict[i]))


# python_frameworks = {
#     "django": {
#         "developer": ['Adrian Holovaty', 'Jacob Kaplan-Moss', 'Simon Willison'],
#         "initial_release": '21 July 2005',
#         "license": '3-clause BSD'
#     },
#     "flask": {
#         "developer": 'Armin Ronacher',
#         "intital_release": "April 1, 2010",
#         "license": 'BSD'
#     },
#     "fast_api": {
#         "developer": '',
#         "initial_release": 'December 5, 2018',
#         "license": 'MIT'
#     }
# }

# for i in python_frameworks:
#     # print(i + ": ", str(python_frameworks[i]))
#     print("*"*80)
#     for j in python_frameworks[i]:
#         print(j + ": " + str(python_frameworks[i][j]))
# print("*"*80)


# print(python_dict.clear())
# copy_python_dict = python_dict.copy()
# copy_python_dict.update({'logo': 'some logo'})
# print(copy_python_dict)
# print(python_dict)

# python_dict.pop('name')
# print(python_dict)
# python_dict.popitem()
# print(python_dict)


# python_frameworks = {'Django', 'Flask', 'Fast API', 'Django'}
# python_frameworks.add('Turtle')
# print(python_frameworks)

# python_frameworks = ('Django', 'Flask', 'Fast API', 'Django')
# print(python_frameworks.count('Django'))
# print(python_frameworks[1:4])
