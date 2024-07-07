from random import randint
import requests
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer
        self.exp = 0
        self.lvl = 1
        self.next = 0
        self.maxexp = 100

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.maxhp = randint(1, 10)
        self.hp = self.maxhp
        self.power = randint(1, 10)

        


        Pokemon.pokemons[pokemon_trainer] = self
        

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API


    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        if isinstance(self, Wizard):
            return f"""Имя твоего покемона: {self.name}
Класс: Волшебник
Уровень: {self.lvl}
Опыт: {self.exp}
Здоровье: {self.hp}
Сила: {self.power}"""
        elif isinstance(self, Fighter):
            return f"""Имя твоего покемона: {self.name}
Класс: Боец
Уровень: {self.lvl}
Опыт: {self.exp}
Здоровье: {self.hp}
Сила: {self.power}"""
        else:
            return f"""Имя твоего покемона: {self.name}
Класс: Покемон
Уровень: {self.lvl}
Опыт: {self.exp}
Здоровье: {self.hp}
Сила: {self.power}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chanсe = randint(1,5)
            if chanсe == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            win = randint(50, 100)
            self.exp += win
            if self.exp >= self.maxexp:
                self.next += 1
                return f"""Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!
Получено опыта: {win}
Доступно новых уровней: {self.next}"""
            else:
                return f"""Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!
Получено опыта: {win}"""

        

    def feed(self):
        self.exp += 50
        self.hp += 10
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        if self.exp >= self.maxexp:
            self.exp = self.exp - self.maxexp
            self.next += 1
            self.maxexp += 50
            return f"Вы покормили покемона.\nОпыт: {self.exp}/{self.maxexp} (Уровней доступно: {self.next})\nЗдоровье: {self.hp}/{self.maxhp}\n\nЧтобы повысить уровень, нажмите /next"
        else:
            return f"Вы покормили покемона.\nОпыт: {self.exp}/{self.maxexp}\nЗдоровье: {self.hp}/{self.maxhp}"
    
    def nextlvl(self): 
        return f"""Выберите улучшение:

Здоровье: {self.maxhp} (+10) /hp
Сила: {self.power} (+10) /power

Осталось улучшений: {self.next}"""
    
    def up_hp(self):
        self.maxhp += 10
        self.hp = self.maxhp
        self.lvl += 1
        self.next -= 1
        return f"""Вы повысили здоровье.
Выберите улучшение:

Здоровье: {self.maxhp} (+10) /hp
Сила: {self.power} (+10) /power

Осталось улучшений: {self.next}"""
    
    def up_power(self):
        self.power += 10
        self.hp = self.maxhp
        self.lvl += 1
        self.next -= 1
        return f"""Вы повысили силу.
Выберите улучшение:

Здоровье: {self.maxhp} (+10) /hp
Сила: {self.power} (+10) /power

Осталось улучшений: {self.next}"""
    
    

class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        superpower = randint(5,15)
        self.power += superpower
        res = super().attack(enemy)
        self.power -= superpower
        return res + f"\nБоец применил супер-атаку силой: {superpower}"
    