import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Holiday Package Predictor",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    preprocessor = joblib.load("preprocessor.pkl")
    return model, preprocessor


model, preprocessor = load_model()


# =========================================================
# CUSTOM CSS - GLASSMORPHISM
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 200, 255, 0.18),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(140, 80, 255, 0.18),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(0, 255, 170, 0.10),
                transparent 30%
            ),
            #07111f;
        color: #ffffff;
    }

    /* Main content */
    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .hero {
        padding: 35px;
        border-radius: 25px;
        margin-bottom: 25px;

        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);

        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);

        box-shadow:
            0 8px 32px rgba(0, 0, 0, 0.35),
            inset 0 1px 0 rgba(255, 255, 255, 0.08);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 10px;
        background: linear-gradient(
            90deg,
            #00e5ff,
            #7c4dff,
            #00ffa3
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        font-size: 17px;
        color: #c8d4e3;
        line-height: 1.7;
    }

    /* Glass cards */
    .glass-card {
        padding: 25px;
        border-radius: 22px;

        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);

        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);

        box-shadow:
            0 8px 30px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.06);

        margin-bottom: 20px;
    }

    .glass-card h2 {
        color: #ffffff;
        margin-bottom: 10px;
    }

    .glass-card p {
        color: #b9c7d8;
        line-height: 1.7;
    }

    /* Feature cards */
    .feature-card {
        padding: 20px;
        border-radius: 18px;

        background: rgba(255, 255, 255, 0.055);
        border: 1px solid rgba(255, 255, 255, 0.10);

        backdrop-filter: blur(15px);

        min-height: 145px;
    }

    .feature-card h3 {
        color: #ffffff;
        margin-bottom: 8px;
    }

    .feature-card p {
        color: #aebed0;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Section titles */
    .section-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;

        color: #ffffff;
    }

    /* Input labels */
    label {
        color: #dce8f5 !important;
        font-weight: 600 !important;
    }

    /* Inputs */
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 55px;

        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.18);

        background: linear-gradient(
            135deg,
            #00bcd4,
            #6755e8
        );

        color: white;
        font-size: 17px;
        font-weight: 700;

        box-shadow:
            0 8px 25px rgba(0, 188, 212, 0.25);

        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0 12px 30px rgba(103, 85, 232, 0.35);
    }

    /* Metric */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 20px;
        border-radius: 18px;
        backdrop-filter: blur(15px);
    }

    [data-testid="stMetricValue"] {
        color: #00e5ff;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(5, 14, 27, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.10);
    }

    /* Hide Streamlit menu */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div class="hero">

        <h1>✈️ Holiday Package Purchase Predictor</h1>

        <p>
            An end-to-end Machine Learning application that predicts whether
            a customer is likely to purchase a holiday package based on
            customer demographics, interaction details, travel behavior,
            and sales-pitch information.
        </p>

        <p>
            Enter the customer's information below and let the trained
            Random Forest Classification model generate a prediction.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PROJECT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">🤖 About This Project</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="glass-card">

    <h2>What does this project do?</h2>

    <p>
    This project is a <b>Holiday Package Purchase Prediction</b> system.
    It uses customer-related information to predict whether a customer
    will purchase a holiday package.
    </p>

    <p>
    The model considers information such as the customer's age,
    occupation, marital status, number of trips, passport status,
    preferred property rating, sales pitch duration, satisfaction score,
    monthly income, and other customer interaction details.
    </p>

    <h2>🧠 Machine Learning Model</h2>

    <p>
    The prediction is performed using a
    <b>Random Forest Classifier</b>.
    Random Forest is an ensemble classification algorithm that combines
    predictions from multiple decision trees to make a final prediction.
    </p>

    <h2>⚙️ Preprocessing</h2>

    <p>
    Before prediction, the input data is passed through the same
    preprocessing pipeline used during model training.
    Categorical variables are encoded using
    <b>One-Hot Encoding</b>, while numerical variables are scaled using
    <b>StandardScaler</b>.
    </p>

    <h2>🎯 Prediction Target</h2>

    <p>
    The model predicts <b>ProdTaken</b>:
    </p>

    <ul>
        <li><b>0</b> → Customer is predicted not to purchase the package</li>
        <li><b>1</b> → Customer is predicted to purchase the package</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MODEL HIGHLIGHTS
# =========================================================

st.markdown(
    '<div class="section-title">📌 Model Highlights</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🌲 Random Forest</h3>
            <p>
            Ensemble machine learning algorithm based on multiple
            decision trees for classification.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🔄 Data Preprocessing</h3>
            <p>
            Categorical data is One-Hot Encoded and numerical data
            is standardized before prediction.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>📊 Probability</h3>
            <p>
            Along with the prediction, the application displays the
            model's estimated purchase probability.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📝 Customer Information</div>',
    unsafe_allow_html=True
)

st.info(
    "💡 Fill in the customer details below. "
    "Hover over the information icons beside each field to understand "
    "what the input represents."
)


with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # LEFT COLUMN
    # -----------------------------------------------------

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30,
            help="Customer's age in years."
        )

        type_of_contact = st.selectbox(
            "Type of Contact",
            ["Self Enquiry", "Company Invited"],
            help="How the customer came into contact with the company."
        )

        city_tier = st.selectbox(
            "City Tier",
            [1, 2, 3],
            help="Classification of the customer's city based on its market tier."
        )

        duration_of_pitch = st.number_input(
            "Duration of Pitch",
            min_value=0,
            value=10,
            help="Duration of the sales presentation/pitch given to the customer."
        )

        occupation = st.selectbox(
            "Occupation",
            ["Salaried", "Small Business", "Free Lancer"],
            help="Customer's occupation or employment category."
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"],
            help="Customer's gender."
        )

        number_of_followups = st.number_input(
            "Number of Followups",
            min_value=0,
            value=3,
            help="Number of follow-up interactions made with the customer."
        )

        product_pitched = st.selectbox(
            "Product Pitched",
            ["Basic", "Deluxe", "King", "Standard", "Super Deluxe"],
            help="Holiday package/product presented to the customer."
        )

        preferred_property_star = st.selectbox(
            "Preferred Property Star",
            [3, 4, 5],
            help="Preferred hotel/property rating of the customer."
        )

    # -----------------------------------------------------
    # RIGHT COLUMN
    # -----------------------------------------------------

    with col2:

        marital_status = st.selectbox(
            "Marital Status",
            ["Married", "Unmarried", "Single", "Divorced"],
            help="Customer's marital status."
        )

        number_of_trips = st.number_input(
            "Number of Trips",
            min_value=0,
            value=3,
            help="Number of trips taken by the customer."
        )

        passport = st.selectbox(
            "Passport",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the customer has a passport. 1 = Yes, 0 = No."
        )

        pitch_satisfaction_score = st.selectbox(
            "Pitch Satisfaction Score",
            [1, 2, 3, 4, 5],
            help="Customer's satisfaction score for the sales pitch. "
                 "1 = Lowest, 5 = Highest."
        )

        own_car = st.selectbox(
            "Own Car",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the customer owns a car. 1 = Yes, 0 = No."
        )

        designation = st.selectbox(
            "Designation",
            ["AVP", "Executive", "Manager", "Senior Manager", "VP"],
            help="Customer's professional designation/category."
        )

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            value=25000.0,
            step=500.0,
            help="Customer's monthly income."
        )

        total_visiting = st.number_input(
            "Total Visiting",
            min_value=0,
            value=2,
            help="Total number of people visiting, calculated from "
                 "the number of persons and children visiting."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🔮 Predict Holiday Package Purchase"
    )


# =========================================================
# PREDICTION
# =========================================================

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

        # Apply the exact preprocessing used during training
        transformed_data = preprocessor.transform(input_data)

        # Model prediction
        prediction = model.predict(transformed_data)[0]

        # Probability
        probability = model.predict_proba(transformed_data)[0][1]

        st.divider()

        st.markdown(
            '<div class="section-title">🔮 Prediction Result</div>',
            unsafe_allow_html=True
        )

        if prediction == 1:

            st.success(
                "🎉 Customer is predicted to purchase the holiday package!"
            )

        else:

            st.warning(
                "❌ Customer is predicted NOT to purchase the holiday package."
            )

        # Probability card
        st.markdown("<br>", unsafe_allow_html=True)

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            st.metric(
                "Purchase Probability",
                f"{probability * 100:.2f}%"
            )

        with result_col2:

            st.metric(
                "Prediction",
                "Purchase" if prediction == 1 else "Not Purchase"
            )

        st.progress(float(probability))

        st.markdown(
            f"""
            <div class="glass-card">

                <h2>📊 What does this probability mean?</h2>

                <p>
                The model estimates a purchase probability of
                <b>{probability * 100:.2f}%</b>.
                </p>

                <p>
                This probability is produced by the trained Random Forest
                classifier based on the customer information provided above.
                It should be interpreted as a model prediction, not a
                guarantee of customer behavior.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error("Prediction failed. Please check the input values.")

        st.exception(e)


# =========================================================
# INPUT GUIDE
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">📚 Input Guide</div>',
    unsafe_allow_html=True
)

input_guide = pd.DataFrame({
    "Input": [
        "Age",
        "Type of Contact",
        "City Tier",
        "Duration of Pitch",
        "Occupation",
        "Gender",
        "Number of Followups",
        "Product Pitched",
        "Preferred Property Star",
        "Marital Status",
        "Number of Trips",
        "Passport",
        "Pitch Satisfaction Score",
        "Own Car",
        "Designation",
        "Monthly Income",
        "Total Visiting"
    ],

    "Meaning": [
        "Customer's age in years.",
        "How the customer contacted or was contacted by the company.",
        "Market tier/category of the customer's city.",
        "Duration of the sales pitch given to the customer.",
        "Customer's occupation category.",
        "Customer's gender.",
        "Number of follow-up interactions with the customer.",
        "Holiday package presented to the customer.",
        "Hotel/property star rating preferred by the customer.",
        "Customer's marital status.",
        "Number of trips taken by the customer.",
        "Whether the customer has a passport.",
        "Customer's satisfaction score for the sales pitch.",
        "Whether the customer owns a car.",
        "Customer's professional designation.",
        "Customer's monthly income.",
        "Total number of people visiting."
    ]
})

st.dataframe(
    input_guide,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <br>

    <div style="
        text-align:center;
        color:#8191a5;
        padding:25px;
        font-size:14px;
    ">

        ✈️ <b>Holiday Package Purchase Prediction</b>
        <br><br>

        Built with Python • Pandas • Scikit-learn • Streamlit
        <br>

        Machine Learning Model: Random Forest Classifier

    </div>
    """,
    unsafe_allow_html=True
)
