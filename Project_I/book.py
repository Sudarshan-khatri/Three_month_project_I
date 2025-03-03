#This program to use to enter the book list in file ,update the books and delete the book in the system.
import random
import json


def book_id():
    id_list=[1,2,3,4,5,6,7,8,9,0]
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
                "year":self.year.strftime("%x"),
                "version":self.version
            }
            with open("book_data.json","a") as file1:
                json.dump(data,file1)
                file1.write("\n")
            print("data stored in json file")
            
        except FileNotFoundError:
            print("Data not stored in file")


class delete_book(add_book):
    def __init__(self,b_id):
        self.b_id=str(b_id)

    def delete(self):
        try:
            with open("book_data.json","r") as file2:
                data=json.load(file2)
            # match the data and remove the book 
            found=False
            for book in data:
                if book["id"]==self.b_id:
                    data=data.remove(book)
                    found=True
                    break
        
            if found:
                with open("book_data.json","w") as file2:
                    json.dump(data,file2,indent=2)
                print(f"Book id {self.b_id} deleted sucessfully !!!")
            else:
                print(f"Book id {self.b_id} not found !!!!")

        except FileExistsError:
            print("Data not found !!!!!!")


class update_book(delete_book):
    pass



