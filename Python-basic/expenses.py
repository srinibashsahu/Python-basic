# expense = [10,50,8,6,5,20,3]
#sum=0
# for expen in expense:
#     sum=sum+expen

# total = sum(expense)

# print('you spent $', total, sep = '')

expenses = []
num = int(input("enter number of expenses you want"))
for i in range(num):
    print(i)
    expenses.append(float(input("Enter the expemse:\n")))

total = sum(expenses)
print('you spent $', total, sep = '')