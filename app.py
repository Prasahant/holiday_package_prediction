import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Holiday Package Predictor",
    page_icon="✈️",
    layout="wide"
)

@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    preprocessor = joblib.load("preprocessor.pkl")
    return model, preprocessor

model, preprocessor = load_artifacts()

# Exact columns used by the fitted preprocessor
CAT_COLS = ['TypeofContact', 'Occupation', 'Gender', 'ProductPitched', 'MaritalStatus', 'Designation']
NUM_COLS = ['Age', 'CityTier', 'DurationOfPitch', 'NumberOfFollowups', 'PreferredPropertyStar', 'NumberOfTrips', 'Passport', 'PitchSatisfactionScore', 'OwnCar', 'MonthlyIncome', 'TotalVisiting']
CATEGORIES = {'TypeofContact': ['Company Invited', 'Self Enquiry'], 'Occupation': ['Free Lancer', 'Large Business', 'Salaried', 'Small Business'], 'Gender': ['Female', 'Male'], 'ProductPitched': ['Basic', 'Deluxe', 'King', 'Standard', 'Super Deluxe'], 'MaritalStatus': ['Divorced', 'Married', 'Unmarried'], 'Designation': ['AVP', 'Executive', 'Manager', 'Senior Manager', 'VP']}

st.title("✈️ Holiday Package Purchase Predictor")
st.markdown(
    "Enter the customer details below to predict whether the customer "
    "is likely to purchase the holiday package."
)

st.divider()

# Keep the same feature names as the training notebook.
with st.form("prediction_form"):
    st.subheader("Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0.0, value=30.0, step=1.0)
        type_of_contact = st.selectbox(
            "Type of Contact", CATEGORIES["TypeofContact"]
        )
        city_tier = st.number_input(
            "City Tier", min_value=1, value=1, step=1
        )
        duration_of_pitch = st.number_input(
            "Duration of Pitch", min_value=0.0, value=10.0, step=1.0
        )
        occupation = st.selectbox(
            "Occupation", CATEGORIES["Occupation"]
        )
        gender = st.selectbox(
            "Gender", CATEGORIES["Gender"]
        )
        number_of_followups = st.number_input(
            "Number of Followups", min_value=0.0, value=3.0, step=1.0
        )
        product_pitched = st.selectbox(
            "Product Pitched", CATEGORIES["ProductPitched"]
        )
        preferred_property_star = st.number_input(
            "Preferred Property Star", min_value=0.0, value=3.0, step=1.0
        )

    with col2:
        marital_status = st.selectbox(
            "Marital Status", CATEGORIES["MaritalStatus"]
        )
        number_of_trips = st.number_input(
            "Number of Trips", min_value=0.0, value=3.0, step=1.0
        )
        passport = st.selectbox(
            "Passport", [0, 1]
        )
        pitch_satisfaction_score = st.number_input(
            "Pitch Satisfaction Score", min_value=1.0, max_value=5.0,
            value=3.0, step=1.0
        )
        own_car = st.selectbox(
            "Own Car", [0, 1]
        )
        designation = st.selectbox(
            "Designation", CATEGORIES["Designation"]
        )
        monthly_income = st.number_input(
            "Monthly Income", min_value=0.0, value=25000.0, step=500.0
        )
        total_visiting = st.number_input(
            "Total Visiting", min_value=0.0, value=2.0, step=1.0
        )

    submitted = st.form_submit_button(
        "🔮 Predict Purchase", use_container_width=True
    )

if submitted:
    input_data = pd.DataFrame({
        "Age": [age],
        "TypeofContact": [type_of_contact],
        "CityTier": [city_tier],
        "DurationOfPitch": [duration_of_pitch],
        "Occupation": [occupation],
        "Gender": [gender],
        "NumberOfFollowups": [number_of_followups],
        "ProductPitched": [product_pitched],
        "PreferredPropertyStar": [preferred_property_star],
        "MaritalStatus": [marital_status],
        "NumberOfTrips": [number_of_trips],
        "Passport": [passport],
        "PitchSatisfactionScore": [pitch_satisfaction_score],
        "OwnCar": [own_car],
        "Designation": [designation],
        "MonthlyIncome": [monthly_income],
        "TotalVisiting": [total_visiting]
    })

    try:
        # Apply the SAME fitted preprocessing used during model training.
        transformed_data = preprocessor.transform(input_data)

        prediction = int(model.predict(transformed_data)[0])

        st.divider()
        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("🎉 The customer is predicted to purchase the package.")
        else:
            st.warning("❌ The customer is predicted not to purchase the package.")

        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(transformed_data)[0][1])
            st.metric("Purchase Probability", f"{probability * 100:.2f}%")

            st.progress(probability)

    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)

with st.expander("Model information"):
    st.write("Model: Random Forest Classifier")
    st.write(f"Raw input features: {len(CAT_COLS) + len(NUM_COLS)}")
    st.write(f"Categorical features: {len(CAT_COLS)}")
    st.write(f"Numerical features: {len(NUM_COLS)}")
