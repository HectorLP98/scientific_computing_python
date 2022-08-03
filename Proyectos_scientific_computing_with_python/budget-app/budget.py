class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []
        self.saldo = 0
        
    def deposit(self, cantidad, description=''):
        self.ledger.append({"amount":cantidad, "description": description})
        self.saldo += cantidad
        
        
    def withdraw(self, cantidad, description=''):
        if self.saldo >= cantidad:
            self.ledger.append({"amount": -cantidad, "description": description})
            self.saldo -= cantidad
            return True
        else:
            return False
        
    def get_withdraw(self):
        # total retirado
        get_withdraw = self.ledger[0]['amount']-self.get_balance()
        return get_withdraw
        
    def get_balance(self):
        return self.saldo
    
    #transfer(transfer_amount, self.entertainment)
    def transfer(self, cantidad, objeto):
        if self.check_funds(cantidad):
            desc = "Transfer to " + objeto.name
            self.withdraw(cantidad, desc)
            objeto.deposit(cantidad, 'Transfer from '+self.name)
            return True
        else:
            return False
        
    def check_funds(self, cantidad):
        if self.saldo >= cantidad:
            return True
        else:
            return False
    
    def __str__(self):
        string_title = self.name
        string_ledger= string_title.center(30, '*') +'\n'
        for i in self.ledger:
            string_ledger+=f'{i.get("description")[:23]:23}' + f'{i.get("amount"):7.2f}' + '\n'
        string_ledger+= f'Total: {self.get_balance()}'
        

        return string_ledger
        

def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    withdrawals = []
    for name in categories:
        withdrawals.append(name.get_withdraw())
        
    percent_withdrawal = [round(i / sum(withdrawals) * 100) for i in withdrawals]
    names = [cat.name.lower().capitalize() for cat in categories]
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percent_withdrawal:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += ' ' * 4 + '-' * (2 * (len(categories) + 1) + 2)
    max_len = len(max(names, key=len))
    names = [i.ljust(max_len) for i in names]
    for i in range(max_len):
        chart += '\n     '
        for name in names:
            chart += name[i] + '  '

    return chart