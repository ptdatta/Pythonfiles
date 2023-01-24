"""
File IO Basics

"r"->open file for reading(default)
"w"->open a file for writing
"x"->creats file if not eicts
"a"->add more content to a file
"t"->text mode.It deals with the file data as a string.(default)
"b"->binary mode
"+"->read and write
"""

# f=open("Parthib","rt")
# # c=f.read(10)
# # c=f.read()
# # print(f.readline())
# print(f.readlines())
# # for i in f:
# #     print(i)
# f.close()
#
# f=open("Parthib","w")
# a=f.write("Parthib will be a procoder")
# print(a)      #returns characters you write
# f.close()


#read,write and append mode
# f=open("Parthib","r+")
# a=f.write("hellodhehdh djj\n")
# print(f.read())
# f.write("thank u")
# f.close()

# f=open("Parthib")
# print(f.tell())         #tell the position of file pointer
# print(f.readline())
# f.seek(10)              #reset the position of file pointer
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# f.close()


# open file with blocks
with open("Parthib") as f:       #no need to close the file
    print(f.read(5))
    print(f.readlines())
