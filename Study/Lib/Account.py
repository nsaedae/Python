
class Account:

    # 속성 : 생성자에서 선언
    def __init__(self, bank, id, name, balance):
        self.bank = bank
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def show(self):
        print('-'*20)
        print('은행명 :', self.bank)
        print('계좌번호 :', self.id)
        print('입금주 :', self.name)
        print('현재잔액 :', self.balance)
        print('-' * 20)






