import pandas as pd
# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatures.append(int(row[1]))
# 		print(row)
# print(temperatures)

df = pd.read_csv("weather_data.csv")

print(df["temp"].max())

print(df[df.day == "Monday"])

def f(x):
	x = x * (9/5) + 32
	return float(x)
	
print(df[df.day == "Monday"].temp.apply(f))

#create dataframe from scratch
data_dict = {
	"students": ["Amy", "James", "Angela"],
	"scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")