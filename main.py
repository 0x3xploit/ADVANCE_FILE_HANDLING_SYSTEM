import socket
import random
import os
from time import *

class Files:

    def layout():
        print("==================================")
        print("   ADVANCE FILE HANDLING SYSTEM")
        print("==================================")

    def choice():
        print("     [1] Display All The Files ")
        print("     [2] Display File")
        print("     [3] Create File")
        print("     [4] Edit File")
        print("     [5] Delet File")
        print("     [6] Advance Option")
        print("     [7] About")
        print("     [8] Exit")

    def inpt():
        inpt=int(input("    Enter Your Choice :: "))
        return inpt

    def Display_ALL():
        PATH = "C:/Users/User/PycharmProjects/BCA_FILE_HANDLING_PROJECT"
        PATH2="C:/Users/User/PycharmProjects"
        print("Display All Function ")
        ALL_FILES=os.listdir(PATH)
        print("===========================")
        print("      ALL THE FILES")
        print("===========================")
        for entry in ALL_FILES:
            print("     ",entry)
        print("============================")
        n = input("       Enter 1 to Go Back :: ")
        if n == '1':
            return 1
        else:
            return 1

    def Display_File():
        print("Display  file function")
        PATH="C:/Users/User/PycharmProjects/BCA_FILE_HANDLING_PROJECT"
        file_name=input("       Enter the name of th file :: ")
        try:
            file=open(file_name,'r')
            print("===========================")
            print("  CONTENT OF THE FILE")
            print("===========================")
            for i in file:
                print(i)
            print("===========================")
            n = input("       Enter 1 to Go Back :: ")
            if n == '1':
                return 1
            else:
                return 1
        except:
            print("Enable To Open The File")
            return 1

    def Creat_File():
        print("Create File Function")
        file_name=input("         Enter the Name Of the File :: ")
        file=open(file_name,'w')
        x=ctime()
        file.write("File Created On ::-")
        file.write(x)
        print("File Created Sucessfully....!! ")
        file.close()
        n = input("       Enter 1 to Go Back :: ")
        if n == '1':
            return 1
        else:
            return 1

    def Edit_File():
        print("Edit file function")
        file_name=input("       Enter the File Name :: ")
        file=open(file_name,'a')
        edit_contet=""
        edit_contet=input("Enter Your Content Hear :: ")
        file.write(edit_contet)
        print("File Edite Sucessfuly....!!")
        file.close()
        n = input("       Enter 1 to Go Back :: ")
        if n == '1':
            return 1
        else:
            return 1

    def Delet_File():
        print("Delet file ")
        file_name=input("       Enter The Name of the File :: ")
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("     File does not exist....!!")
        print("     File Deleted Sucesfully....!!")
        n = input("       Enter 1 to Go Back :: ")
        if n == '1':
            return 1
        else:
            return 1

    def Advance_op():
        print("Advance file function")

        n = input("       Do You Want to start the connection (Y/N) :: ")
        if n == 'N' or n == 'n':
            return 1
        elif n == 'Y' or n == 'y':
            return 0
        else:
            return 1

    def About():
        print("===================About===================")
        print("   [*] What is File Handling System ?")
        print("         It is a System in which we")
        print("         can creat,Display,Edit")
        print("         Delet & Watch the Files")
        print("   [*] Whats New ?")
        print("       We can Trasfer Files over ")
        print("       WAN (Wi-Fi) !! ")
        print("   [*] CREATED BY :-")
        print("        [*] {MR ERROR}")
        print("===========================================")
        n = input("       Enter 1 to Go Back :: ")
        if n == '1':
            return 1
        else:
            return 1

def cho():
    var = obj_file.inpt()
    if var == 1:
        a=obj_file.Display_ALL()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 2:
        a=obj_file.Display_File()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 3:
        a=obj_file.Creat_File()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 4:
        a=obj_file.Edit_File()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 5:
        a=obj_file.Delet_File()
        if a==1:
            obj_file.choice()
            con()
        elif a==0:
            ob.Start_Connection()
        else:
            obj_file.choice()
            con()
    elif var == 6:
        a=obj_file.Advance_op()

        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 7:
        a=obj_file.About()
        if a == 1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var==8:
        print("Exited")
        exit(0)
    else:
        cho()

class Connection():
    def Start_Connection():
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST="192.168.235.131"
        PORT=random.randint(1000,9999)
        try:
            s.bind((HOST,PORT))
            print("Connection has been setup on :-")
            print(f"HOST :: {HOST}")
            print(f"PORT :: {PORT}")
            print("Wating For VICTIM to CONNECT !!")
            s.listen(2)
            c, address=s.accept()
            print("VICTIM Connected Sucessfully !!")
            print("[1] Transfer Files")
            print("[2] Transfer Images")
            n=str(input("Enter Your Choice :: "))
            if n=='1':
                r=1
                while r!=0:
                    c.send(bytes(n,'utf-8'))
                    file_name=str(input("Enter the name of the file :: "))
                    try:
                        file_data=open(file_name,'rb')
                        send_data=file_data.read(1024)
                        c.send(send_data)
                        print("File Sended sucessfully")
                        n=input("Do You Want To Send Another File (Y/N) :: ")
                        if n=='Y' or n=='y':
                            r=1
                        elif n=='N' or n=='n':
                            r=0
                            Files.layout()
                            Files.choice()
                            Files.inpt()
                            cho()
                        else:
                            r=0
                    except:
                        print("Enable to open the file")
            elif n=='2':
                c.send(bytes(n, 'utf-8'))
                img_name= str(input("Enter the name of the file :: "))
                try:
                    img_data = open("sen.jpg", 'rb')
                    send_data = img_data.read(2048)
                    while send_data:
                        c.send(send_data)
                        img_data=img_data.read(2048)
                    print("File Sended sucessfully")
                except:
                    print("Enable to open the file")
                c.send(bytes(n,'utf-8'))

            elif n=='3':
                print("Connection Closed")
                c.close()
            else:
                print("Connection Closed")
                c.close()
        except:
            print("     [*] Enable to connect ")
            print("     [*] Make sure that you are connected to same Wi-Fi Network")
            p=input("       Press 1 to go back")
            if p=='1':
                Files.layout()
                Files.choice()
                cho()
ob=Connection
def c_n():
    ob.Start_Connection()

obj_file=Files
obj_file.layout()
obj_file.choice()
def con():
    var = obj_file.inpt()
    if var == 1:
        a=obj_file.Display_ALL()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 2:
        a=obj_file.Display_File()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 3:
        a=obj_file.Creat_File()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 4:
        a=obj_file.Edit_File()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 5:
        a=obj_file.Delet_File()
        if a==1:
            obj_file.choice()
            con()
        elif a==0:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 6:
        a=obj_file.Advance_op()
        c_n()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var == 7:
        a=obj_file.About()
        if a==1:
            obj_file.choice()
            con()
        else:
            obj_file.choice()
            con()
    elif var==8:
        print("Exited Sucessfully")
        exit(0)
    else:
        choice()
con()
