# class Vehicle:
#     def __init__(self, name, color, type, wheel, seat, speed):
#         self.name = name
#         self.color = color
#         self.type = type
#         self.wheel = wheel
#         self.seat = seat
#         self.speed = speed

#     def information(self):
#         print("Vehicle's name: " + self.name)
#         print("Vehicle's color: " + self.color)
#         print("Vehicle's type: " + self.type)
#         print("Vehicle's wheel: " + str(self.wheel)) 
#         print("Vehicle's seat: " + str(self.seat))
#         print("Vehicle's speed: " + str(self.speed))


#     def tinh_van_toc(self):
#         return self.wheel * self.seat + self.speed



# car = Vehicle("Mercedes", "white", "car", 4, 4, 300)
# bike = Vehicle("BMW", "black", "bicycle", 2, 2, 10)


# car.information()
# print("Van toc car:", car.tinh_van_toc())

# bike.information()
# print("Van toc bike:", bike.tinh_van_toc())

# # 67
# # class Champion:
# #     def __init__(self, name, lane, role, hp, mana):
# #         self.name = name
# #         self.lane = lane
# #         self.role = role
# #         self.hp = hp
# #         self.mana = mana

# #     def intrinsic(self):
# #         print(self.name + " uses passive")

# #     def Q(self):
# #         print(self.name + " uses Q")

# #     def W(self):
# #         print(self.name + " uses W")

# #     def E(self):
# #         print(self.name + " uses E")

# #     def R(self):
# #         print(self.name + " uses R (ultimate)")

# #     def info(self):
# #         print("name:", self.name)
# #         print("lane:", self.lane)
# #         print("role:", self.role)
# #         print("HP:", self.hp)
# #         print("mana:", self.mana)

# # champ = Champion("Zed", "mid", "assassin", 600, 200)

# # champ.info()
# # champ.Q()
# # champ.W()
# # champ.E()
# # champ.R()

# class Champion:
#     def __init__(self, name, lane, role, hp, mana):
#         self.name = name
#         self.lane = lane
#         self.role = role
#         self.hp = hp
#         self.mana = mana
#         self.items = []

#     def info(self):
#         print("name:", self.name)
#         print("lane:", self.lane)
#         print("role:", self.role)
#         print("HP:", self.hp)
#         print("mana:", self.mana)
#         print("items:", self.items)

#     def add_items(self):
#         for i in range(6):
#             item = input("item " + str(i+1) + ": ")
#             self.items.append(item)

# champ = Champion("Zed", "mid", "assassin", 600, 200)

# champ.add_items()
# champ.info()

# bai1
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def say_hi(self):
#         print("hi my name is " + self.name + ".")

#     def tell_position(self):
#         print("i am a " + self.position + ".")


# john = Employee("john", "software Engineer")

# john.say_hi()
# john.tell_position()

# bai2
# class Rectangle:
#     def __init__(self, h, w):
#         self.h = h
#         self.w = w

#     def perimeter(self):
#         return 2 * (self.h + self.w)

#     def area(self):
#         return self.h * self.w


# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def perimeter(self):
#         return 2 * 3.14 * self.r

#     def area(self):
#         return 3.14 * self.r * self.r


# shape = input("shape (rectangle|circle): ")

# if shape == "rectangle":
#     h = int(input("height: "))
#     w = int(input("width: "))
#     obj = Rectangle(h, w)

# elif shape == "circle":
#     r = int(input("radius: "))
#     obj = Circle(r)

# else:
#     print("invalid!")
#     exit()

# print("perimeter:", obj.perimeter())
# print("area:", obj.area())

# bai3
# from datetime import datetime

# class CustomDate:
#     def __init__(self):
#         self.now = datetime.now()

#     def get_date(self):
#         return self.now.strftime("%d/%m/%Y")

#     def get_time(self):
#         return self.now.strftime("%H:%M:%S")


# d = CustomDate()

# print(d.get_date())
# print(d.get_time())

# bai4
# from datetime import datetime

# class DateHandler:
#     def format_date(date):
#         return date.strftime("%d/%m/%Y")

#     def get_days_between(date1, date2):
#         return (date2 - date1).days


# start_date = datetime(2021, 1, 1)
# end_date = datetime(2022, 1, 1)

# print("start:", DateHandler.format_date(start_date))
# print("end:", DateHandler.format_date(end_date))
# print("days between:", DateHandler.get_days_between(start_date, end_date))