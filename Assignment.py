import json
with open('precipitation.json') as file:
    data = json.load(file)
#print(data)

precipitation={}
#selecting only the Seattle data
seatle_precipitations = []
for city in data:
    if city['station'] == 'GHCND:US1WAKG0038':
        seatle_precipitations.append(city)
        #print(seatle_precipitations)

#Here I want to select the month for each 'date'
#I'm selecting the string for 'date' in the original dictionary and separating it by '-'. Then I select the second element of that string i.e the month number
splitted_date =[]
for city in seatle_precipitations:
    city['date'].split('-')[1]
    split_by_month=city['date'].split('-')[1]

    new_dic={   #Here I am creating a new dictionary with the elements I need: the months and the values for each month
    'month': split_by_month,
    'value': city['value']
    }
    splitted_date.append(new_dic)
#print(splitted_date)

#to find out the precipitation per month I first have to group per month and then i summarise the values for each month
sum_months_values = {}
for i in splitted_date:
    month = i['month']
    if month not in sum_months_values:
        sum_months_values[month] = 0
        sum_months_values[month] += i['value']
print(sum_months_values)
     
#saving to JASON

precipitation['Seattle'] = {'station': 'GHCND:US1WAKG0038',
        'state': 'WA',
        'total_monthly_precipitation': sum_months_values
         }
    
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation, file, indent=4)
