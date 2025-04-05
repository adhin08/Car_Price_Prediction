import numpy as np
import pickle
import json

class Prediction:
    def __init__(self):
        print("Initializing Prediction Model")

    def load_raw(self):
        # Load the model, column names, and encoded data
        with open("D:/CAR_PRICE_PRED/app/Car_Pred_Model.pkl", "rb") as model_file:
            self.model = pickle.load(model_file)

        with open("D:/CAR_PRICE_PRED/app/Column.json", "r") as col_file:
            self.col = json.load(col_file)

        with open("D:/CAR_PRICE_PRED/app/encoded_data.json", "r") as enc_file:
            self.encoded_data = json.load(enc_file)

        return "Load Raw Success"

    def predict_price(self, data):
        self.load_raw()
        self.data = data

        user_input = np.zeros(len(self.col["column_names"]))
        array = np.array(self.col["column_names"])

        # Extracting the data from user input
        manufacturer = self.data['Manufacturer']
        car_category = self.data['Car_Category']
        fuel_type = self.data['Fuel_Type']
        color = self.data['Color']
        engine_volume = self.data['Engine_Volume']
        mileage = self.data['Mileage']
        transmission = self.data['Transmission']
        doors = self.data['Number_of_Doors']
        turbo = self.data['Turbo']
        leather_interior = self.data['Leather_Interior']
        drive_wheels = self.data['Drive_Wheels']
        cylinders = self.data['Cylinders']
        airbags = self.data['Airbags']

        # Encoding and filling the user input array based on categorical data
        # Ensure the appropriate encoding logic is applied for categorical features
        user_input[array == "Manufacturer_" + manufacturer] = 1
        user_input[array == "Category_" + car_category] = 1
        user_input[array == "Fuel type_" + fuel_type] = 1
        user_input[array == "Color_" + color] = 1
        user_input[array == "Transmission_" + transmission] = 1
        user_input[array == "Doors_" + str(doors)] = 1
        user_input[array == "Turbo_" + str(turbo)] = 1
        user_input[array == "Leather_Interior_" + str(leather_interior)] = 1
        user_input[array == "Drive_wheels_" + drive_wheels] = 1

        # Numerical features like engine volume, mileage, cylinders, airbags
        user_input[array == "Engine_Volume"] = float(engine_volume)
        user_input[array == "Mileage"] = float(mileage)
        user_input[array == "Cylinders"] = int(cylinders)
        user_input[array == "Airbags"] = int(airbags)

        # Predicting the price
        predicted_price = self.model.predict([user_input])[0]

        return predicted_price
