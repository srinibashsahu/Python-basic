age = int(input("how old you are?\n"))
# decade = age/10
decade = age//10
year = age%10
print("you are belogs to " + str(decade) + "decades " +  str(year) +"years old")