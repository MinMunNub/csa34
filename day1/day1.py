class Vehicle:
    def __init__(self, name, color, type, wheel, seat, speed):
        self.name = name
        self.color = color
        self.type = type
        self.wheel = wheel
        self.seat = seat
        self.speed = speed

    def information(self):
        print("Vehicle's name: " + self.name)
        print("Vehicle's color: " + self.color)
        print("Vehicle's type: " + self.type)
        print("Vehicle's wheel: " + str(self.wheel)) 
        print("Vehicle's seat: " + str(self.seat))
        print("Vehicle's speed: " + str(self.speed))


    def tinh_van_toc(self):
        return self.wheel * self.seat + self.speed



car = Vehicle("Mercedes", "white", "car", 4, 4, 300)
bike = Vehicle("BMW", "black", "bicycle", 2, 2, 10)


car.information()
print("Van toc car:", car.tinh_van_toc())

bike.information()
print("Van toc bike:", bike.tinh_van_toc())

# 67
# class Champion:
#     def __init__(self, name, lane, role, hp, mana):
#         self.name = name
#         self.lane = lane
#         self.role = role
#         self.hp = hp
#         self.mana = mana

#     def intrinsic(self):
#         print(self.name + " uses passive")

#     def Q(self):
#         print(self.name + " uses Q")

#     def W(self):
#         print(self.name + " uses W")

#     def E(self):
#         print(self.name + " uses E")

#     def R(self):
#         print(self.name + " uses R (ultimate)")

#     def info(self):
#         print("name:", self.name)
#         print("lane:", self.lane)
#         print("role:", self.role)
#         print("HP:", self.hp)
#         print("mana:", self.mana)

# champ = Champion("Zed", "mid", "assassin", 600, 200)

# champ.info()
# champ.Q()
# champ.W()
# champ.E()
# champ.R()

class Champion:
    def __init__(self, name, lane, role, hp, mana):
        self.name = name
        self.lane = lane
        self.role = role
        self.hp = hp
        self.mana = mana
        self.items = []

    def info(self):
        print("name:", self.name)
        print("lane:", self.lane)
        print("role:", self.role)
        print("HP:", self.hp)
        print("mana:", self.mana)
        print("items:", self.items)

    def add_items(self):
        for i in range(6):
            item = input("item " + str(i+1) + ": ")
            self.items.append(item)

champ = Champion("Zed", "mid", "assassin", 600, 200)

champ.add_items()
champ.info()

