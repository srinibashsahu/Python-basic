def find_acronym():
    look_up=input("what acronym you are looking for\n")
    found=False
    try:
        with open('input.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found=True
                    break

        if not found:
            print("Not found")
    except FileNotFoundError as e:
        print("file not found")

def add_acronym():
    acronym= input("what acronym you want to add\n")
    defination= input("what is the defination\n")
    with open('input.txt','a') as file:
        file.write('\n'+acronym+ '-'+ defination)

def main():
    user_choice=input("you want to add or read acronym")
    if user_choice=='add':
        add_acronym()
    else:
        find_acronym()

main()