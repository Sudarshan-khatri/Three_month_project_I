"""This  program  help to view the list of  book in library and search the book and purchase the book from 
library .student.py file help to  show the student protion"""

from Project_I.mod import*

class student_profile:
    def __init__(self,s_id,user_name,grade,faculty,section):
        self.s_id=s_id
        self.user_name=user_name
        self.grade=grade
        self.faculty=faculty
        self.section=section
    
    def student_details(self):
        try:

        #dictionary to store the details of students
            s_data={
                "s_id":self.s_id,
                "s_user_name":self.user_name,
                "s_grade":self.grade,
                "s_stream":self.faculty,
                "s_sect":self.section
            }
        #store the data in json file:
            with open("student_data.json","a") as s_file1:
                json.dump(s_data,s_file1)
                print("\n")
            print("Data stored sucessfully !!!")

        except FileExistsError:
            print("File not found !!!!")

class view_book(student_profile,add_book):
    def __init__(self, book_id):
        self.book_id=book_id
    """This function is used to view the book list by student or purchase the book from the library.It work 
    by checking the option if option is 1 then view the book and if option is 2 then purchase the book.If
    purchase the book then delete from the library data list and store in the purchase book list"""
    def view_or_purchase(self):
        print("\n\n\t\t\twelcome to library".upper())
        print("\t\t\tA:view books".upper())
        print("\t\t\tB:purchase book".upper())
        student_option=int(input("Enter the choice:"))
        if(student_option==1):
            #condition 1 to show all the data of the book stored in the library
            try:
                with open("book_data.json","r") as std_view:
                    data=json.load(std_view)
                    
                #show all data 
                for book in data:
                    print(book)

            except FileNotFoundError:
                print("sorry file not opned !!!")
            
            #condition 2to purchase the book from library:
        elif(student_option==2):
                """This option help to purchase the book if the student and  book id match """
                try:
                    found=False
                    with open("book_data.json","r") as bfile:
                        book=json.load(bfile)
                    for data in book:
                        if data["id"]==self.b_id:
                            found=True
                            break
                    book_purchase=False
                    if found:
                        with open("student_data.json","r+") as stfile:
                            student_id=json.load(stfile)
                        for s_data in student_id:
                            if s_data["id"]==self.s_id:
                                book_purchase=True
                                break
                    """If the book id and student id match then we store the book details in purchase list and delete from the 
                    book list """
                    if book_purchase:
                        with open("book_data.json","r+") as new_file1:
                            r_book=json.load(new_file1)
                        for r_data in r_book:
                            r_data=r_data.remove(r_data)
                            
                except FileNotFoundError:
                    print("Sorry file not find !!!!")




if __name__=="__main__":
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
                    

            