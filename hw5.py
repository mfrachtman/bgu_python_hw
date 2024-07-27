import random
class Animals:
    age = 0
    satiefy = 100
    def __init__(self, name, name_specie, sex):
        self.sex = sex
        self.name = name 
        self.specie = name_specie
        if self.specie == "медведе-утконос":
            self.food = ["свинобраз", "крольгуру"]
            self.habitat = "earth"
            self.lifespan = 100
            self.size = 10
        elif self.specie == "свинобраз":
            self.food = "grass"
            self.habitat = "earth"
            self.lifespan = 100
            self.size = 5
        elif self.specie == "крольгуру":
            self.food = "grass"
            self.habitat = "earth"
            self.lifespan = 100
            self.size = 7
        elif self.specie == "кротобарсук":
            self.food = "grass"
            self.habitat = "earth"
            self.lifespan = 100
            self.size = 2
        elif self.specie == "драконий лосось":
            self.food = ["рыбожуравль","черепахокраб"]
            self.habitat = "water"
            self.lifespan = 50
            self.size = 4
        elif self.specie == "рыбожуравль":
            self.food = ["черепахокраб","унаги"]
            self.habitat = "water"
            self.lifespan = 50
            self.size = 3
        elif self.specie == "унаги":
            self.food = "grass"
            self.habitat = "water"
            self.lifespan = 50 
            size = 1
        elif self.specie == "черепахокраб":
            self.food = ["черепахокраб", "унаги"]
            self.habitat = "water"
            self.lifespan = 50
            self.size = 2
        elif self.specie == "тигролёт":
            self.food = ["зубролёт","козлолёт"]
            self.habitat = "air"
            self.lifespan = 30
            self.size = 7
        elif self.specie == "зубролёт":
            self.food = ["сумчатая летяга"]
            self.habitat = "air"
            self.lifespan = 25
            self.size = 8
        elif self.specie == "козлолёт":
            self.food = "grass"
            self.habitat = "air"
            self.lifespan = 26
            self.size = 5
        elif self.specie == "сумчатая летяга":
            self.food = "grass"
            self.habitat = "air"
            self.lifespan = 10
            self.size = 1

    def info(self):
        print("пол:", self.sex, "возраст:", self.age, "сытость:", self.satiefy, "%")
    def reproduction(self,partner):
        if self.specie != partner.specie:
            return "на этой планете размножаются только одновидные зверушки"
        if self.sex == partner.sex:
            return "животные однополые. на этой планете размножаются только разнополые ребята"
        if self.habitat == "earth":
            if self.satiefy <= 20 or partner.satiefy <= 20:
                return "один из пары животных голодный и не находит сил для размножения:("
            if self.age < 6 or partner.age < 6:
                return "упс...один из животных пока не дорос до таких вещей"
            print ("юху! поздравляю, на этой планете появились 2 новых представителя! с почином:)")
            for i in range(1, 3):
                n = input("введите" + str(i) + "имя:")
                while n in cur_animals:
                    n = input("опа...а это имя уже занято, попробуйте другое!")
                    cur_animals[n] = Animals(n, self.specie, random.choice("m", "f"))
        elif self.habitat == "water":
            if self.satiefy <= 50 or partner.satiefy <= 50:
                return "один из пары животных голодный и не находит сил для размножения:("
            print ("о-хо-хо...на планете большое пополнение! теперь на ней на 10 особей больше! поздравляю!")
            for i in range(1, 11):
                n = input("введите" + str(i) + "имя:")
                while n in cur_animals:
                    n = input("опа...а это имя уже занято, попробуйте другое!")
                cur_animals[n] = Animals(n, self.specie, random.choice(("m", "f")))
        elif self.habitat == "air":
            if self.satiefy <= 42 or partner.satiefy <= 42:
                return "один из пары животных голодный и не находит сил для размножения:("
            if self.age < 4 or partner.age < 4:
                return "упс...один из животных пока не дорос до таких вещей"
            print ("о-хо-хо...на планете большое пополнение! теперь на ней на 4 особей больше! поздравляю!")
            for i in range(1, 5):
                n = input("введите" + str(i) + "имя:")
                while n in cur_animals:
                    n = input("опа...а это имя уже занято, попробуйте другое!")
                    cur.animals[n] = Animals(n, self.specie, random.choice("m", "f"))
        return ""
def information():
    print("на этой планете живёт 12 видов живности")
    print("медведе-утконос : употребляет свинобразов и крольгуру в пищу, водится на суше, живет 100 лет")
    print("свинобраз : травояден, водится на суше, живет 100 лет")
    print("крольгуру : травояден, водится на суше, живет 100 лет")
    print("кротобарсук: травояден, водится на суше, живет 100 лет")
    print("драконий лосось: употребляет рыбожуравля и черепахокраба в пищу, водится в воде, живет 50 лет")
    print("рыбожуравль : употребляет рыбожуравля и унаги в в пищу, водится в воде, живет 50 лет")
    print("черепахокраб : употребляет себе подобных и унаги в пищу, водится в воде, живет 50 лет")
    print("унаги : травояден, живет в воде, живет 50 лет")
    print("тигролёт : употребляет зубролёта и козлолёта в пищу, водится в воздухе, живет 30 лет")
    print("зубролёт : употребляет сумчатую летягу в пищу, одится в воздухе, живет 25 лет")
    print("козлолёт : травояден, водится в воздухе, живет 26 лет")
    print("сумчатая летяга : травоядна, водится в воздухе, живет 10 лет")
def helpp():
    print("команды:")
    print("/add - добавление особи")
    print("/finish - закончить работу программы")
    print("/food - узнать количество растительной пищи на планете")
    print("/changefood - увеличить количество растительной пищи на планете")
    print("/info - выводить информацию об особи")
    print("/reproduction - размножение")
    print("/plustime - увеличить время на 1")
def time_plus():
    global food_storage
    deaths = []
    for i in cur_animals:
        cur_animals[i].age += 1
        if cur_animals[i].lifespan < cur_animals[i].age:
            food_storage += cur_animals[i].size
            print("особь " + cur_animals[i].name + " умерла от старости, но не стоит отчаиваться, ведь жизнь продолжается!")
            deaths.append(i)
        else:
            if cur_animals[i].food == "grass": 
                if food_storage > 0:
                    food_storage -= 1
                    cur_animals[i].satiefy += 0.26 * cur_animals[i].satiefy
                    if cur_animals[i].satiefy > 100: cur_animals[i].satiefy = 100
                else:
                    cur_animals[i].satiefy -= 0.09 * cur_animals[i].satiefy
            else:
                cur_animals[i].satiefy -= 0.09 * cur_animals[i].satiefy
                for j in cur_animals:
                    if cur_animals[j].specie in cur_animals[i].food:
                        r = random.choice((1, 0))
                        if r == 1:
                            cur_animals[i].satiefy += 0.62 * cur_animals[i].satiefy
                            if cur_animals[i].satiefy > 100: cur_animals[i].satiefy = 100
                            print("особь " + cur_animals[j].name + " съели. очень жаль, но было вкусно!")
                            deaths.append(j)
                            break
                        else:
                            cur_animals[i].satiefy -= 0.16 * cur_animals[i].satiefy
    for i in deaths:
        del cur_animals[i]
    for i in cur_animals:
        if cur_animals[i].satiefy < 10:
            print("особь " + cor_animals[i].name + "умерла от голода. нужно кушать плотно!")
            del cur_animals[i]
    return
def inf():
    global cur_animals, food_storage
    print("живые животные:")
    for i in cur_animals:
        print(cur_animals[i].name)
        cur_animals[i].info()
species = ["медведе-утконос", "свинобраз", "крольгуру", "кротобарсук", "кротобарсук", "рыбожуравль", "драконий лосось", "унаги", "черепахокраб", "тигролёт", "зубролёт", "козлолёт", "сумчатая летяга"]
cur_animals = dict()
time = 0
food_storage = 100
command = 0
information()
helpp()
while command != "/finish":
    command = input() 
    if command == "/add":
        a = input("введите имя особи:")
        while a in cur_animals:
            a = input("это имя уэе занято, попробуйте ещё раз:")
        b = input("введите вид особи:")
        while b not in species:
            b = input("такого вида не существует, попробуйте ещё раз:")
        c = input("введите пол особи(m или f):")
        while c not in["m", "f"]:
            c = input("такого пола не существует, попробуйте ещё раз:")
        cur_animals[a] = Animals(a, b, c)
    elif command == "/food":
        print("количество растительной пищи на планете:", food_storage)
    elif command == "/changefood":
        a = input()
        while not a.isnumeric():
            a = input("введите число")
        food_storage += int(a)
    elif command == "/info":
        a = input("введите имя особи:")
        while a not in cur_animals:
            a = input("такой особи не существует, попробуйте ещё раз:")
        cur_animals[a].info()
    elif command == "/reproduction":
        a = input("введите имя особи:")
        b = input("введите имя особи:")
        while a not in cur_animals or b not in cur_animals:
            print("такой особи не существует, попробуйте ещё раз:")
            a = input("введите имя особи:")
            b = input("введите вид особи:")
        print(cur_animals[a].reproduction(cur_animals[b]))
    elif command == "/plustime":
        time_plus()
        time += 1
    elif command == "/animals":
        inf()
                 

                            


