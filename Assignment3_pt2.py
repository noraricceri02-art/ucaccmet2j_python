import json
with open('precipitation.json') as file:
        data = json.load(file)
    #print(data)

city_dictionary={'Cincinnati':{'station': 'GHCND:USW00093814', 'state': 'OH'},
                 'Seattle':{'station': 'GHCND:US1WAKG0038', 'state': 'WA'},
                 'Maui':{'station': 'GHCND:USC00513317', 'state': 'HI'},
                 'San Diego':{'station': 'GHCND:US1CASD0032', 'state': 'CA'}
}

#I am calculating the overall amount of precipitation
overall_precipitation=0
for value in data:
    overall_precipitation= overall_precipitation + value['value']
#print(overall_precipitation)

precipitation={}
relative_yearly_precipitation=[]

for city_name in city_dictionary:
    #selecting all 4 cityes
    precipitations_per_city = []
    for row in data:
        if row['station'] == city_dictionary[city_name]['station']:
            precipitations_per_city.append(row)
    #print(precipitations_per_city)

    #Here I want to select the month for each 'date'
    #I'm selecting the string for 'date' in the original dictionary and separating it by '-'. Then I select the second element of that string i.e the month number
    splitted_date =[]
    for city in precipitations_per_city:
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
        else:
            sum_months_values[month]+=i['value']

    #print(sum_months_values)
    values_list =list(sum_months_values.values())
    #print(values_list)

    #calculating the total yearly precipitation
    total_yearly_precipitation =0
    for monthly_precipitation in values_list:
        total_yearly_precipitation = total_yearly_precipitation + monthly_precipitation
    #print(total_yearly_precipitation)

    #calculating the relative monthly precipitation 
    list_monthly_precipitation=[]
    for x in values_list:
        relative_yearly_precipitation=x/total_yearly_precipitation
        list_monthly_precipitation.append(relative_yearly_precipitation)
    #print(list_monthly_precipitation)

    #calculating the relative yearly precipitation 
    relative_precipitation_year=total_yearly_precipitation/overall_precipitation
    
    #saving to JASON
    precipitation[city_name] = {'station': city_dictionary[city_name]['station'],
            'state': city_dictionary[city_name]['state'],
            'total_monthly_precipitation': values_list,
            'relative_monthly_precipitation' : list_monthly_precipitation,
            'relative_yearly_precipitation': relative_precipitation_year
            }

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation, file, indent=4)


