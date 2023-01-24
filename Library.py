class library:
     def __init__(self,list,name):
         self.bookslist=list
         self.name=name
         self.lendict={}

     def displaybooks(self):
         print(f"We have following books in our library:  {self.name}")
         for book in self.bookslist:
             print(book)

     def lendbook(self,user,book):
         if book not in self.lendict.keys():
             self.lendict.update({book:user})
             print("Lender book has been updated.You can take the book now")
         else:
             print(f"Book is alraedy taken by {self.lendict[book]}")

     def addbook(self,book):
         self.bookslist.append(book)
         print("book has been added")

     def returnbook(self,book):
         self.bookslist.remove(book)


if __name__=='__main__':
    harry=library(['Python','Rich Dad Poor Dad','The Intelligent Investor','Java Algorithms'],"CodewithHarry")

    while(True):
        print(f"Welcome to {harry.name} library.Enter your choice to continue")
        print("1.Display Book")
        print("2.Lend Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice=int(input())

        if user_choice==1:
            harry.displaybooks()

        elif user_choice==2:
            book=input("Enter the name of the book you want to land:" )
            name=input("Enter your name" )
            harry.lendbook(name,book)


        elif user_choice==3:
            book=input("Enter the name of the book:" )
            harry.addbook(book)

        elif user_choice==4:
            book=input("Enter the book you want to return: " )
            harry.returnbook(book)


        else:
            print("Not a valid option")


        print("press Q to quit and C to continue")
        user_choice2=""
        while(user_choice2!="Q" and user_choice2!="C"):
            user_choice2=input()
            if user_choice2=="C":
                continue
            elif user_choice2=="Q":
                exit()

