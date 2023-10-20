import joblib
import math
print("Program Started")
model = joblib.load('HousePricePredicyion\house_price_prediction_model.joblib')
area = int(input("Enter the area of the house: "))
rooms = int(input("Enter the number of rooms: "))
age = int(input("Enter the age of the house: "))
print("The price of the house is: ")
value = model.predict([[area, rooms, age]])
print(math.floor(value))
print("Program Ended")
