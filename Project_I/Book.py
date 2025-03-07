#This program to use to enter the book list in file ,update the books and delete the book in the system.
import random
import json
from colorama import Fore
from datetime import datetime


def book_id():
    id_list=[1,2,3,4,5,6,7,8,9]
    digit=(random.sample(id_list,3))
    id_number = "".join(map(str, digit))
    return id_number

class add_book:
    def __init__(self,id,title,author,year,version):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.version=version

    def add_book_in_file(self):
        try:
            data={
                "id":self.id,
                "title":self.title,
                "author":self.author,
                "year":self.year.isoformat(),
                "version":self.version
            }

        
            book_list = []

            try:
                with open("book_data.json", "r") as file1:
                    for line in file1:
                        book_list.append(json.loads(line.strip()))  # Read existing books
            except FileNotFoundError:
                print("File not found, creating a new one.")

            # Append new book data
            book_list.append(data)

            # Write data back in JSONL format (one JSON object per line)
            with open("book_data.json", "w") as file1:
                for book in book_list:
                    json.dump(book, file1)
                    file1.write("\n")  # Write new line to separate entries

            print("Book data stored successfully.")

        except Exception as e:
            print(f"Error: {e}")


class delete_book(add_book):
    def __init__(self,b_id):
        self.b_id=str(b_id)


    def delete(self):
        try:
            # Read books from file
            with open("book_data.json", "r") as file2:
                books = [json.loads(line.strip()) for line in file2]

            # Check if book exists
            original_length = len(books)
            books = [book for book in books if book["id"] != self.b_id]

            if len(books) == original_length:
                print(f"Book ID {self.b_id} not found!")
                return

            # Write updated list back to file
            with open("book_data.json", "w") as file2:
                for book in books:
                    json.dump(book, file2)
                    file2.write("\n")  # Keep JSONL format

            print(f"Book ID {self.b_id} deleted successfully!")

        except FileNotFoundError:
            print("No books found in the file2!")
        except json.JSONDecodeError:
            print("Error reading book data!")


if __name__=="__main__":
     #First login the admin then perform the following operation:
        id=input("Enter the admin id:")
        password=input("Enter the admin password:")
        if (id=="admin" and password=="admin"):
            print("Login sucessfully !!!")
            #To run the program multiple time:
            Run_time=1
            while Run_time:
                print(Fore.CYAN+"\n\n\t\t\twelcome to admin portal".upper())
                print("\t\t\t1:add book".upper())
                print("\t\t\t2:delete book".upper())
                print("\t\t\t3:Exit".upper()+Fore.RESET)
                choice_operation=int(input("Enter the operation:"))
                if(choice_operation==1):
                    Book_title=input("Enter the book_title:")
                    Book_author=input("Enter the book author:")
                    time=datetime.now()
                    print(f"Date:{time}")
                    Book_id=book_id()
                    print(f"Book_id:{Book_id}")
                    Book_version=input("Enter the book version:")
                    obj1=add_book(Book_id,Book_title,Book_author,time,Book_version)
                    obj1.add_book_in_file()


                elif(choice_operation==2):
                    #instance for the class delete:
                    try:
                        with open("book_data.json","r") as file2:
                              books = [json.loads(line.strip()) for line in file2]  #Read all books properly
                        #Details of book 
                        print("\nLists of Book:")
                        for book in books:
                            if isinstance(book, dict):
                                print(f"ID: {book.get('id')}, Title: {book.get('title')}, Year: {book.get('year')}, Author: {book.get('author')}, Version: {book.get('version')}")
                            else:
                                print("Invalid book data format.")
                        
                        b_id=int(input("Enter the book id:"))
                        book_obj=delete_book(b_id)
                        book_obj.delete()
                    except FileNotFoundError:
                        print("File of data not found !!!!!")
                else:
                    print("sorry ! Invalid operation")
                    break

        else:
            print("Invalid user_name or password !!!!")

