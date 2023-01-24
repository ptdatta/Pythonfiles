# def myfunc():
#     print("Code With Harry")
#     while True:
#         value = (yield)
#         print(value)
#
# coroutine =myfunc()
# next(coroutine)
# coroutine.send("Python")
# coroutine.send(" Tutorial ")
# coroutine.close()


def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")
search.send("harry")
input("press any key")
search.send("harry and")
input("press any key")
search.send("thi si")
input("press any key")
search.send("joker")
input("press any key")
search.send("like this video")
search.close()
