current_movey= {'The Enenger': '11:00PM',
                'Rudolof': '1:00PM',
                'DDLJ': '3:00PM'}
print('we are showing following movies :')
for mov in current_movey:
    print(mov)

movie= input("which movey you want to see \n")
time= current_movey.get(movie)
if time:
    print("movie time for ", movie, 'is :', time)
else:
    print('we do not have your ',movie)

menus= {'breakfast': ["egg", "sandwitch", "salad"],
        'lunch':['rice', 'biriyani', 'dal' , 'papad'],
        'dinner': ['roti', 'rice', 'biriyani']}
for name, item in menus.items():
    print(name,':',item)