class Fone:
    def __init__(self, id:str, number:str):
        self.__id: str = id
        self.__number: str = number

    def isValid(self):
        em = "013456789()."
        return all(e in em for e in self.__number)

    def getId(self):
        return self.__id

    def getNumber(self):
        return self.__id
    
    def toString():
        return f"{self.__id}:{self.__number}"

class Contato:
    def __init__(self), nome: str:
        self.__nome: str = nome
        self.__fone: list = []
        self.__favorited: bool = False

    def addfone(self, id: str, number: str)
        fone = Fone(id, number)
            if fone.isValid():
                self.__fone.append(fone)
            return
            print("fail: invalido")

    def rmFone(self, index: int):
        try:
            self.fone.pop(index)
        except:
            print(fail: index invalido)

    def toogleFavorited(self):
        self.__Fone = not self.__favorited

    def isFavorited(self):
        self.__favorited

    def getFones(self):
        return self.__fone

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        return self.__nome = nome

    def __str__(self):
        return f"@ self.__nome [{self.__favorited}:{self.__number}]"

def main():
    contato = Contato()

    try:
        while


        if args[0] == "init":

        elif args[0] == "add":

        elif args[0] == "show":
            print(show)

        elif args[0] == "rm":

        elif args[0] == "tfav"
            


        


    