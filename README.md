# 🚗 Car Price Prediction

This project uses Machine Learning to predict the price of a car based on various features like brand, year, fuel type, kilometers driven, and more.

## 📁 Project Structure

```
CAR_PRICE_PRED/
├── app/
│   ├── Car_Pred_Model.pkl
│   ├── Column.json
│   ├── encoded_data.json
│   └── utils.py
├── artifacts/
│   └── Car_Price_Prediction.ipynb
├── car_price_prediction.csv
├── main.py
├── templates/
│   └── index.html
├── CONFIG.py
├── requirements.txt
└── README.md
```

## ⚙️ How it works

- The model is trained using a dataset of car listings.
- It's deployed using Flask.
- Users can input car details via a simple HTML form and receive predicted car prices.

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## 🚀 Run the app

```bash
python main.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000/`

## 🧐 Prediction Features

- Year
- Present Price
- Kms Driven
- Fuel Type
- Seller Type
- Transmission
- Owner
- Car Name

## 💡 ML Model

- Algorithm: `RandomForestRegressor`
- Trained model file: `Car_Pred_Model.pkl`

## ✨ Author

**Adhin C**  
🔗 [GitHub Profile](https://github.com/adhin08)
