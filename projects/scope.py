name = "Buse"

def name_define():
    #name in local just creates a new variable in local scoope
    name = "Çınar"
    print(name)

name_define()

count = 1

def number_define():
    #global says that count is the global count = 1
    global count
    color = "blue"
    print(count)

    def color_define():
        #nonlocal says that go to the parent and get the variable
        nonlocal color
        print(color)
    color_define()

number_define()
