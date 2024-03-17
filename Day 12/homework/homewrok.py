info = []

name = input("Please enter your name:")
lastname = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
hometown = input("Please enter your home town: ")

info.append(name)
info.append(lastname)
info.append(age)
info.append(hometown)

print(info)
print(info[0:2])
print(info[1:3])
print(info[0:3])
print(info[1:])

