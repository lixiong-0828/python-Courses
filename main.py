# 说明：这个python程序，可以接受用户输入的内容，保存到文件上。
#       提供【追加：add,new】，【删除:del, complete】，【显示:show】等功能
import os
#Import from same dir file
#from functions import get_contents,write_to_file

#if want import from other folder like [./module] ,can use like bellow.
from module.functions import get_contents, write_to_file

while True:

    user_input = input("Enter  add XXX(or new), del XXX(or delete), show, edit XXX, exit: ")
    if user_input.startswith("add") or user_input.startswith("new"):

        user_input = user_input[4:]
        if user_input == '':
            print("You did not enter a item.Pls Enter again.")
            continue

        if os.path.exists("./output/output_file.txt") :

            contents = get_contents()
            contents.append(f"{user_input} \n")

            write_to_file(contents)

        else:
            contents =[]
            contents.append(f"{user_input} \n")
            write_to_file(contents)

    elif user_input.startswith("del") or user_input.startswith("delete") :

        if os.path.exists("./output/output_file.txt"):

            contents = get_contents()
            print("---------------------------------")
            print("Current contents from output file :")
            print("--------------")

            for line in contents:
                print(line.strip("\n"))
            print("---------------------------------")
        else:
            print("Sorry, Not found output file.")

        edit_num = input("Enter the number of edit Item  (like: 1 ): ")

        if edit_num.isdigit():
            edit_num = int(edit_num) - 1
        else:
            print("Please enter a number.")

        contents.pop(edit_num)

        write_to_file(contents)

    elif user_input.startswith("show"):

        if os.path.exists("./output/output_file.txt"):

            contents = get_contents()
            if len(contents) < 1:
                print("It's empty file.")
                continue

            print("---------------------------------")
            print("contents from output file :")
            print("-----------")
            for index,line in enumerate(contents):
                print(f"{index}-{line.strip("\n")}")
            print("---------------------------------")
        else:
            print("Not found output file.")

    elif user_input.startswith("edit"):

        if os.path.exists("./output/output_file.txt"):

            contents = get_contents()

            print("---------------------------------")
            print("Current contents from output file :")
            print("--------------")
            for line in contents:
                print(line.strip("\n"))
            print("---------------------------------")
        else:
            print("Sorry, Not found output file.")

        edit_num = input("Enter the number of edit Item  (like: 1 ): ")

        if edit_num.isdigit():
            edit_num = int(edit_num) - 1
        else:
            print("Please enter a number.")

        edit_content = input("Enter the name of new item (like:new item): ")

        if edit_content == '':
            print("You did not enter a item.Pls Enter again.")
            continue

        contents[edit_num] = edit_content + '\n'

        write_to_file(contents)

    elif user_input.startswith("exit"):
        break
    else:
        print("Invalid input.")
        continue

