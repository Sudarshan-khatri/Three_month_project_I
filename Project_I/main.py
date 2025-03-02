"""This is the first project of three month backend class using the concept of basic python and 
oop in python .The project tittle is "Personal Library management system" .It has following functionlity
#Adding the Book
#Views the Books
# Search the Books
#Updates the Books
# Delete the books"""

from colorama import Fore
import book as bk
import student as std


def main():
    print(Fore.GREEN+"\n\n\t\twelcome personal library management system".upper())
    print("\t\t1:Admin".upper())
    print("\t\t2:student".upper()+Fore.RESET)
    choice=int(input("User status:".upper()))
    match choice:
        case 1:
            id=input("Enter the admin id:")
            password=input("Enter the admin password:")
            if (id=="admin" and password=="admin"):
                print("Login sucessfully !!!")
        case 2:
            pass
        

    print("\n\n\n\n\n")


if __name__==" __main__":
    main()