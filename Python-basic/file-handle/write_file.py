acronym= input("what acronym you want to add\n")
defination= input("what is the defination\n")
with open('input.txt','a') as file:
    file.write('\n'+acronym+ '-'+ defination)