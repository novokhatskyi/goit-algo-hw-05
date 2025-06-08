from rich import print
from rich.prompt import Prompt


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def remove_key_value(self, key):
        key_hash = self.hash_function(key)
        for index, pair in enumerate(self.table[key_hash]):
            if pair[0]  == key:
                del self.table[key_hash][index]
                return True
        return False
    
    def __str__(self):
        return str(self.table)



# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30
print(H)

quest = Prompt.ask("Чи є необхідність ву видаленні даних з таблиці? Y/N")
if quest.lower() == "y":
    key = Prompt.ask("[bold green]Введіть ключ для видалення х таблиці[/bold green]").lower()
    result = H.remove_key_value(key)
    if result:
        print("[green]Запис видалено[/green]")
    else:
        print("[red]Ключ не знайдено[/red]")
else:
    print("[bold blue]Good Bye[/bold blue]")
print(H)
