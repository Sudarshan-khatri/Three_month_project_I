"""This is the first project of three month backend class using the concept of basic python and 
oop in python .The project tittle is "Personal Library management system" .It has following functionlity
#Adding the Book
#Views the Books
# Search the Books
#Updates the Books
# Delete the books"""

from colorama import*

def main():
    try:
        print("sorry")
        print(Fore.GREEN+"\n\n\t\twelcome personal library management system".upper())
        print("\t\t1:Admin".upper())
        print("\t\t2:student".upper()+Fore.RESET)
        choice=int(input("User status:".upper()))
        match choice:
            case 1:
                #First login the admin then perform the following operation:
                id=input("Enter the admin id:")
                password=input("Enter the admin password:")
                if (id=="admin" and password=="admin"):
                        print("Login sucessfully !!!")
                        print(Fore.CYAN+"\n\n\t\t\twelcome to admin portal".upper())
                        print("\t\t\t1:add book".upper())
                        print("\t\t\t2:update book".upper())
                        print("\t\t\t3:delete book".upper()+Fore.RESET)
                        choice_operation=int(input("Enter the operation:"))
                        if(choice_operation==1):
                            Book_title=input("Enter the book_title:")
                            Book_author=input("Enter the book author:")
                            x=datetime.datetime.now()
                            print(f"Id_no:{book_id()}")
                            Book_version=input("Enter the book version:")
                            obj1=add_book(book_id(),Book_title,Book_author,x,Book_version)
                            obj1.add_book_in_file()


                        elif(choice_operation==2):
                            #instance for the class delete:
                            try:
                                with open("book_data.json","r") as file2:
                                    books=json.load(file2)
                                    #Details of book 
                                    print("\nLists of Book:")
                                    for book in books:
                                        print(f"ID:{book['id']},Tittle:{book['title']},Year:{book['year']},Author:{book['author']},Version:{book['version']}")
                                    b_id=int(input("Enter the book id:"))
                                    book_obj=delete_book(b_id)
                                    book_obj.delete()
                            except FileNotFoundError:
                                print("File of data not found !!!!!")

            case 2:
                    try:
                        print("\n\n\t\t\tWELCOME TO STUDENT PORTAL")
                        print("\t\t\t1:register student".upper())
                        print("\t\t\t2:student library".upper())
                        option=int(input("Choose the option:"))
                        if(option==1):
                            # Data of student taken for registeration:
                            std_name=input("Enter student name:")
                            std_grade=int(input("Enter the grade:"))
                            std_faculty=input("Enter the faculty:")
                            std_sec=input("Enter the section:")
                            #create an instance of class student_profile
                            std_obj1=student_profile(book_id(),std_name,std_grade,std_faculty,std_sec)
                            std_obj1.student_details()
                               
                                
                    except :
                        print("code not run error !!")

        print("\n\n\n\n\n")
    except:
        print("System not work !!!!")


if __name__==" __main__":
    main()