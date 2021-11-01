# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
años_restantes= 90-int(age)

x = 365 * int(años_restantes)
y = 52 * int(años_restantes)
z = 12 * int(años_restantes)

print("You have {} days, {} weeks, and {}months left.".format(x,y,z))
