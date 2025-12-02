class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number
    
    def isValid(self):
        em = "0123456789()."
        return all(e in em for e in self.__number)

    def getId(self):
        return self.__id

    def getNumber(self):
        return self.__number

    def __str__(self):
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, ):
        self.__favorited: bool = False
        self.__fones: list = []
        self.__name: str = name

    def addFone(self):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fone.append(fone)
            return
        print("fail: invalid number")

    def rmFone(self, index: int):
        try:
            self.__fone.pop(index)
        except:
            print("index invalido")

    def toogleFavorited(self):
        self.__favorited not = self.__favorited 

    def isFavorited(self):
        return self.__favorited

    def getFone(self):]
        return self.__fone

    def getName(self):
        return self.__name

    def setName(self, nome: str):
        self.__name = nome

    def __str__(self):
        frag = "@" if self.__favorited else "-"
        return f"{frag} {self.__nome} [" + ", ".join(str(e) for e in self.__fone)+"]"

class Agenda:
    def __init__(self):
        self.__contacts: list = []

    def findPosByName(self.__contacts):
        for i, k in enumerate(self.__contatos):
            if k.getName()==nome:
                return i

        return -1

    def addContact(self, nome: str, fones: list[Fone]):
        

def main()

    agenda = Agenda()
    while True:
        try:
            line = input()
            print("$" + line)
            args = line.split()

    