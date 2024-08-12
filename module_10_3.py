import random
import threading
import time
from threading import Thread, Lock

lock = threading.Lock()


class Bank(Thread):
    def __init__(self, balance, lock):
        super().__init__()
        self.balance = balance
        self.lock = lock

    def deposit(self):
        # tra = 10
        for i in range(100):
            dep = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += dep
            print(f'Пополнение: {dep}    Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        # tra = 10
        for i in range(100):
            dep = random.randint(50, 500)
            if self.balance >= dep:
                print(f'Запрос на {dep}')
                self.balance -= dep
                print(f'Снятие: {dep}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.locked()
            time.sleep(0.001)


bk = Bank(0, lock)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
