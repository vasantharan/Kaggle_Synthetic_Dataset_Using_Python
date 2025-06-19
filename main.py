import numpy as np
import pandas as pd

np.random.seed(42)

dataset_file = 'House Price Prediction.csv'

def generate_data(n):
    bedrooms = np.random.randint(1,4, size=n)
    bathrooms = np.random.randint(1,3, size=n)
    location_rating = np.random.randint(1,5, size=n)
    sqrt = np.random.randint(800,4000, size=n)
    house_age = np.random.randint(0,100, size=n)
    price = ((bedrooms*50000) + (bathrooms*10000) + (sqrt*20000) + (location_rating*1000) - (house_age*3000))
    price = np.clip(price, 50000, None)
    return bedrooms, bathrooms, sqrt, location_rating, house_age, price

n = 1000

bedrooms, bathrooms, sqrt, location_rating, house_age, price = generate_data(n)

data = pd.DataFrame({
    "Bedrooms" : bedrooms,
    "Bathrooms": bathrooms,
    "Square Feet": sqrt,
    "House Age": house_age,
    "Location Rating": location_rating,
    "Price (USD)" : price
})

data.to_csv(dataset_file, index=False)
print('Dataset created')