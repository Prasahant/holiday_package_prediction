# Holiday Package Prediction - Streamlit Frontend

This frontend uses the exact trained artifacts supplied for the project:

- `model.pkl` - trained Random Forest classifier
- `preprocessor.pkl` - fitted preprocessing pipeline

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app collects the 17 raw input features, applies the fitted preprocessor,
and sends the transformed data to the trained Random Forest model.

Categorical features detected from the fitted preprocessor:
TypeofContact, Occupation, Gender, ProductPitched, MaritalStatus, Designation

Numerical features detected from the fitted preprocessor:
Age, CityTier, DurationOfPitch, NumberOfFollowups, PreferredPropertyStar, NumberOfTrips, Passport, PitchSatisfactionScore, OwnCar, MonthlyIncome, TotalVisiting
