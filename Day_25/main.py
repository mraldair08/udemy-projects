import pandas
# #with open("weather_data.csv") as file:
# #    data = file.readlines()
# #    print(data)
    
# # import csv

# # with open ("weather_data.csv") as data_file:
# #     data = csv.reader(data_file) 
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# # print(temperatures)
# #dataframe = todo el documento
# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])
# #data_dict = data.to_dict()
# #print(data_dict)

# #Series = una columna
# temp_list = data ["temp"].to_list()
# #print(temp_list)
# #average = sum(temp_list) / len(temp_list)
# #mean = data["temp"].mean()
# #print(average)
# #print(mean)
# #print(max(temp_list))

# #get Data in columns
# #print(data["condition"])
# #print(data.condition)

# #get data in row
# #print(data[data.day == 'Monday'])
# #print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# celsius = monday.temp[0]
# faremheit = celsius * 9/5 + 32
# #print(monday.temp)
# print(type(celsius))
# print(faremheit)

#Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 63]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")