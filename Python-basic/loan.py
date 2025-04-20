# Get detail of loan
money_owed = float(input("How much money owed\n"))
apr = float(input("Annumal Pecent rate\n"))
payment= float(input("How much money you pay in each month\n"))
month= int(input("How man y month you want to see\n"))
monthy_rate=apr/100/12

for i in range(month):
    intrest_paid= money_owed*monthy_rate
    money_owed= money_owed +intrest_paid
    money_owed= money_owed- payment
    print('paid',payment, 'of which ', intrest_paid, 'was intrest',end='')
    print('now i owe:',money_owed)
    if(money_owed<=0):
        print('last payment was :',money_owed)
        print("you paid of your loan in ",i+1,'month')
        break