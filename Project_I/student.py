"""This  program  help to view the list of  book in library and search the book and purchase the book from 
library .student.py file help to  show the student protion"""

import json
import main
from book import add_book
class student_profile:
    def __init__(self,id,user_name,grade,faculty,section):
        self.id=id
        self.user_name=user_name
        self.grade=grade
        self.faculty=faculty
        self.section=section
    
    def student_details(self):
        try:

        #dictionary to store the details of students
            s_data={
                "s_id":self.id,
                "s_user_name":self.user_name,
                "s_grade":self.grade,
                "s_stream":self.faculty,
                "s_sect":self.section
            }
        #store the data in json file:
            with open("student_data.json","a") as s_file1:
                json.dump(s_data,s_file1)
                s_file1("\n")

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
        student_option=input("Enter the choice:")
        match student_option:
            #case A to show all the data of the book stored in the library
            case A:
                try:
                    with open("book_data.json","r") as std_view:
                        data=json.load(std_view)
                    
                    #show all data 
                    for book in data:
                        print(book)

                except FileNotFoundError:
                    print("sorry file not opned !!!")
            
            #case B to purchase the book from library:
            case B:
                pass

        