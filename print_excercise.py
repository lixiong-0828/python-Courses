# print("=========dir(list)========",dir(list))
# print("=========help(list.count)========",help(list.count))
#================================
# for i in buttons:
#     print(i.capitalize())
#
# buttons = ["cancel", "reply", "submit"]
#================================
# string_a = ("hello world, "
#             "and this is "
#             "my string")
# print(string_a)
#
# string_b = ("hello world, "
#             "and this is "
#             "my string")
# print(string_b)
#================================
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for filename in filenames:
#     file = open(filename,"w")
#     file.write("Hello World!")
#     file.close()
#================================
# filenames = ['1.doc', 'my.report', 'our.presentation']
# filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
# print(filenames)
#================================
# temperatures = [10, 12, 14]
# file = open("./files/file.txt", 'w')
# for temperature in temperatures:
#     file.writelines(str(temperature) + '\n')
#     # file.write('\n')
# file.close()
#================================
# numbers = [10.1, 12.3, 14.7]
# numbers = [float(number) for number in numbers]
# print(numbers)
import csv
#================================
#
# file = open("./files/file.txt", "w")
# file.write("Hello World")
#
# print('ok')

# with open("./files/file.txt") as file:
#     print(file.read())

#
# with open("./files/file.txt" ,'w') as file:
#     file.write("welcome xiong")

# with open("./files/file.txt" ,'r') as file:
#     print(file.read())
#================================
# languages = ['English', 'German', 'Spanish']
#
# for item in languages:
#     with  open(f"{item}.txt", "w") as file:
#         # TODO: write code...
#         file.write(item)

# #================================ DICT
# dict_1 = {
#     "name": "xiong",
#     "age": 22,
#     "height": 70,
#     "weight": 80,
#     "job": "Engineer",
#     "hobbies": [
#         "python",
#         "programming",
#     ]
# }
#
# print(f"dict_1 :{dict_1}")
# print(dict_1["name"])
# print(f"dict_1.values() : {dict_1.values()}")
# print(f"dict_1.keys() : {dict_1.keys()}")
# print(f"dict_1.items() : {dict_1.items()}")
# print(f"type(dict_1) : {type(dict_1)}  ")
# print(f"type(dict_1.values()) : {type(dict_1.values())}")
# print(f"type(dict_1.keys()) : {type(dict_1.keys())}")
#
# #isalpha() and isalnum()
# print(dict_1["name"].isalpha())
# print(dict_1["name"].isalnum())
# # need to convert to string
# print(str(dict_1["age"]).isalpha())
# print(str(dict_1["age"]).isalnum())

#================================ DICT

# a = 6
# match a:
#     case 5 :
#         print("a is 5")
#     case 6 :
#         print("a is 6")
#     # error : cat't logic or check
#     # case a > 7:
#     #     print("a is 7")
#================================ DICT
# try:
#     value = float(input("pla enter todal"))
#     total_value = float(input("pla enter todal"))
#
#     if total_value == 0:
#         print("Your total value cannot be zero.")
#
#     division = value / total_value

# except ZeroDivisionError:
#     print("Your total value cannot be zero.")
# ==============================================

# try :
#     value = float(input("pla enter todal :"))
#     total_value = float(input("pla enter todal :"))
#
#     if total_value == 0:
#         print("Your total value cannot be zero.")
#         exit()
#
#     division = value / total_value
# except ValueError:
#     print("You did not enter a number.")
# except ZeroDivisionError:
#     print("Your total value cannot be zero.")
# ==============================================
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)
# ==============================================
# def get_average():
#     print("Hi")
#     x = "hello"
#
# # print(get_average())
# ============================================== split

# print("you-and-me".split('-'))  # rsult: ['you', 'and', 'me']
# print("good morning sir".split(' '))  # rsult :['good', 'morning', 'sir']

# ============================================== strip
# print("sample.txt".strip('.txt')) # rsult: sample
#
# # it's cant exactly cut off '.txt'..you can use replace()
# print("test.txt".strip('.txt'))   # rsult: es
#
# # ============================================== replace
#
# print("test.txt".replace('.txt',''))  # rsult: test
# # ==============================================
# def strength(password):
#     length = False
#     if len(password) >= 8:
#         length = True
#
#     isupper = False
#     for i in password:
#         if i.isupper():
#             isupper = True
#             break
#
#     isdigit = False
#     for i in password:
#         if i.isdigit():
#             isdigit = True
#             break
#
#     if length and isupper and isdigit:
#         return "Strong Password"
#     else:
#         return "Weak Password"
# # ==============================================
#
# list_a = [13, 27, 38,78]
# average = sum(list_a) / len(list_a)
# print(average)

# # ==============================================
# def concatenates(param):
#     new_pram = ''
#     for item in param:
#         new_pram =new_pram + item
#     return new_pram
#
# print(concatenates(['345','assdfd','sdf']))

# # ==============================================
# def prepare(text):
#     text = text.title()
#     text = text.strip()
#     return text
#
#
# print(prepare("hello    "))
# # ==============================================

# def my_str(param_1 ="default param 1", param_2 ="default param 2", param_3='default param 3' ):
#     """This function will return the contents of the filepath."""
#     return str(param_1) + "\n" + str(param_2) + "\n" + str(param_3)

# print(my_str('first','second','third'))
# print(my_str('first','second'))
# print(my_str('first'))
# print(my_str())
#
# print(my_str(param_3='param3',param_2='param2',param_1='param1'))
# print(my_str(param_2='param2',param_1='param1'))
# print(help(my_str))
# # ==============================================

# text_01 = """
# It's can be write multiple line
# with out breakdown code
# python default understand
# """
#
# text_02 = "\
# It's can be write one line. \
# deferent form text_01. \
# python default understand\
# "
# print(text_01)
# print(text_02)

# # ==============================================

# def parse(args):
#     len = float(args[0])
#     width = float(args[1])
#     high = float(args[2])
#
#     return len,width,high
#
# args = [6,7,8]
# length,width,high = parse(args)
# print(f"length: {length}, width: {width}, high: {high}")
#
# args_tuple = parse(args)
# print(f"args_tuple: {args_tuple}")
# print(f"args_tuple[0]: {args_tuple[0]}")
# print(f"args_tuple[1]: {args_tuple[1]}")
# print(f"args_tuple[2]: {args_tuple[2]}")

# def len_str(param):
#     if len(param) < 8:
#         return False
#     else:
#         return True

# # ==============================================
# def water_state(temperature):
#     if temperature <= 0:
#         return "Solid"
#     elif temperature > 0 and temperature < 100:
#         return "Liquid"
#     else:
#         return "Gas"
#
# print(water_state(1))
# print(water_state(200))
# print(water_state(-1))
# # ============================================== glob

# import glob
# myfiles = glob.glob("files/*.txt")
#
# for myfile in myfiles:
#     print(f"==== filename: {myfile} ====")
#     with open(myfile, "r") as file:
#         contents = file.read()
#     print(contents)

# # ============================================== csv
# import glob
# mycsv = glob.glob("files/*.csv")
# for mycsv in mycsv:
#     print(f"==== filename: {mycsv} ====")
#     with open(mycsv, "r") as file:
#         contents = list(csv.reader(file))
#     for item in contents:
#         print(item)
# ============================================== shutil

# import shutil
#
# shutil.make_archive('files', 'zip', "files")

# ============================================== webbrowser
import webbrowser

#webbrowser.open('https://docs.python.org/3/tutorial/datastructures.html')

# user_want = input("Enter a website: ")
# webbrowser.open("https://"+user_want)

# user_want = input("What would you like to search for from google? : ")
# webbrowser.open("https://www.google.com.hk/search?q="+user_want)

# ============================================== type of dict

# dic2 = [{'first key': 'key of first' ,'first value': ['value1','value2','value3']},
#         {'second key': 'key of second' ,'second value': ['value1','value2','value3']}]
#
# print(dic2)
# print(type(dic2)) #type of list (list with [])
# print(type(dic2[0]))  # type of dict (dict with {} )
#
# dic2[0]['correct answer'] = 2
# dic2[1]['correct answer'] = 3
#
# print(dic2)

# ==============================================

print("reset main branch")
print("reset main branch-second")