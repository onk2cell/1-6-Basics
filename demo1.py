import os
import csv

class Leagger():
    def __init__(self,amount,type,account,name,note,holder,debtcred):
        self.amount = input("Enter the amount")
        self.type = input("Enter the type")
        self.account = input("account type ")
        self.name = input("name of giver")
        self.note = input("anyspecial note")
        self.holder = input("name of taker")
        self.debtcred = input("given or taken")
    

class createnew(Leagger):
    def __init__(self, amount, type, account, name, note, holder, debtcred,filename):
        self.filename = input("Enter the file name you want to store the data")
        super().__init__(amount, type, account, name, note, holder, debtcred)

    def write_to_csv(self):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.holder, self.account, self.name, self.note, self.debtcred, self.amount])

        


one = createnew("200","pos","bank","onkar","pinetable","sangita","ced","SONA")
one.write_to_csv()







