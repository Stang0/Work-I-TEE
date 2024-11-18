class inventory:
    def __init__(self):
        self._ID = []
        self._name = []
        self._quantity = []
        self._price = []
        self._totalValue = []


    def Get(self):
        with open('inventory.txt', 'r') as file:
            Contents = file.read().splitlines()
            for i in Contents:
                Split = i.split()
                self._ID.append(Split[0])
                self._name.append(Split[1])
                self._quantity.append(int(Split[2]))
                self._price.append(int(Split[3]))
                self._totalValue.append(int(Split[2]) * int(Split[3]) )
            return self._ID , self._name , self._quantity , self._price , self._totalValue
    def Create(self,InventoryList):
        with open('inventory_report.txt', 'w') as file:
            totalValue = 0
            head = (f"""PRODUCT INVENTORY REPORT \n""")
            coloum = (f"""{'Name':<10}{'QUANTITY':<10}{'PRICE':<10}{'TOTAL VALUE':<10} \n""")
            symbo = (f"""{'====':<10}{'=======':<10}{'======':<10}{'=========':<10} \n""")
            file.write(head)
            file.write(coloum)
            file.write(symbo)
            for i in InventoryList:
                line = (f"""{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<10} \n""")
                file.write(line)
                totalValue += i[4]
            file.write('=================================\n')
            result = (f'total value = {str(totalValue)}')
            file.write(result)

def load_inventory():
    ID , name , quantity , price, totalValue = inventory().Get()
    InventoryList = zip(ID , name , quantity , price , totalValue)
    return InventoryList

def generate_report(InventoryList):
    inventory().Create(InventoryList)

def main():
    InventoryList = load_inventory()
    generate_report(InventoryList)


if __name__ == '__main__':
    main()
