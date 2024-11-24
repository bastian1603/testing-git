class nyoba:
    a = 1
    
    def __init__(self):
        self.__class__.a += 1


a = nyoba()
b = nyoba()

print(nyoba.a)