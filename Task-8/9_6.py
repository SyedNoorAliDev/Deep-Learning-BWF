from NinePointOne import Restaurant
class IceStall(Restaurant):
    def __init__(self,res_name,cuis_type):
        super().__init__(res_name,cuis_type)
        self.flavours = []
    def addFlav(self,flav):
        self.flavours.append(flav)
    def printFlavs(self):
        print(self.flavours)
print("IceStall class:-")
Is = IceStall("AlBaik","Arab")
Is.addFlav("Orange")
Is.addFlav("Strawberry")
Is.printFlavs()

        
        
