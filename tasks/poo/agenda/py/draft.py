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
    def __init__(self, name: str):
        self.__favorited: bool = False
        self.__fones: list = []
        self.__name: str = name

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
            return
        print("fail: invalid number")

    def rmFone(self, index: int):
        try:
            self.__fones.pop(index)
        except:
            print("index invalido")

    def toogleFavorited(self):
        self.__favorited = not self.__favorited 

    def isFavorited(self):
        return self.__favorited

    def getFone(self):
        return self.__fones

    def getName(self):
        return self.__name

    def setName(self, nome: str):
        self.__name = nome

    def __str__(self):
        frag = "@" if self.__favorited else "-"
        return f"{frag} {self.__name} [" + ", ".join(str(e) for e in self.__fones)+"]"

class Agenda:
    def __init__(self):
        self.__contatos = []

    def findPosByName(self, nome: str):
        for i, k in enumerate(self.__contatos):
            if k.getName()==nome:
                return i

        return -1

    def addContact(self, nome: str, fones: list[Fone]):
        em = self.findPosByName(nome)

        if em != -1:
            contato = self.__contatos[em]
        else:
            contato = Contact(nome)
            self.__contatos.append(contato)
        
        for i in fones:
            if i.isValid():
                contato.addFone(i.getId(), i.getNumber())
            else:
                print("fail: invalid number {i}")
        self.__contatos.sort(key = lambda c: c.getName())

    def getContact(self, nome: str):
        em = self.findPosByName(nome)
        if em == -1:
            return None
        return self.__contatos[em]

    def search(self, pattern: str):
        encontrado = []
        for contato in self.__contatos:
            if pattern in str(contato):
                encontrado.append(contato)
        return encontrado

    def rm(self, nome: str):
        em = self.findPosByName(nome)
        if em == -1:
            return None
        self.__contatos.pop(em)

    def rmFone(self, nome: str, index: int):
        contato = self.getContact(nome)
        if contato:
            contato.rmFone(index)
        else:
            print("fail: contato não existe")

    def getFavorited(self):
        co = []
        for self._contatos in self._favorited:
            co.append(self.__contatos)
            return self.__favorited
    
    def favs(self):
        return "\n".join(str(c) for c in self.__contatos if c.isFavorited())

    def __str__(self):
        return "\n".join(str(c) for c in self.__contatos)


def main():

    agenda = Agenda()
    while True:
            line = input()
            print("$" + line)
            args = line.split()

            if args[0] == "end":
                break

            elif args[0] == "add":
                nome = args[1]
                fone=[]
                for i in args[2:]:
                    try:
                        id, number=i.split(":")
                        fone.append(Fone(id, number))
                    except ValueError:
                        print(f"fail: invalid phone format: {i}")
                agenda.addContact(nome, fone)

            elif args[0] == "show":
                print(agenda)

            elif args[0] == "rm":
                agenda.rm(args[1])

            elif args[0] == "rmFone":
                agenda.rmFone(args[1], int(args[2]))
            
            elif args[0] == "tfav":
                contato = agenda.getContact(args[1])
                if contato:
                    contato.toogleFavorited()
            
            elif args[0] == "favs":
                print(agenda.favs())

            elif args[0] == "search":
                e = agenda.search(args[1])
                for i in e:
                    print(i)
            else:
                print("comando invalido")

main()

    