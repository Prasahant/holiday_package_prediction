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
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

/* =====================================================
   MAIN APPLICATION
   ===================================================== */

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0, 190, 255, 0.18),
            transparent 30%
        ),

        radial-gradient(
            circle at 90% 20%,
            rgba(120, 70, 255, 0.18),
            transparent 30%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(0, 255, 170, 0.10),
            transparent 30%
        ),

        #07111f;

    color: white;
}


/* =====================================================
   CONTENT WIDTH
   ===================================================== */

.block-container {

    max-width: 1250px;

    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =====================================================
   HERO CARD
   ===================================================== */

.hero {

    padding: 40px;

    border-radius: 25px;

    margin-bottom: 30px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.03)
        );

    border: 1px solid rgba(255,255,255,0.15);

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.08);
}


/* Hero title */

.hero-title {

    font-size: 44px;

    font-weight: 800;

    margin-bottom: 18px;

    background:
        linear-gradient(
            90deg,
            #00e5ff,
            #7c4dff,
            #00ffa3
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


/* Hero description */

.hero-description {

    font-size: 17px;

    color: #c8d4e3;

    line-height: 1.8;

    margin-bottom: 12px;

}


/* =====================================================
   GLASS CARD
   ===================================================== */

.glass-card {

    padding: 28px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.07),
            rgba(255,255,255,0.03)
        );

    border: 1px solid rgba(255,255,255,0.12);

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.25),
        inset 0 1px 0 rgba(255,255,255,0.06);

    margin-bottom: 25px;

}


/* =====================================================
   GLASS FEATURE CARD
   ===================================================== */

.feature-card {

    padding: 22px;

    border-radius: 18px;

    min-height: 155px;

    background:
        rgba(255,255,255,0.055);

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(15px);

    box-shadow:
        0 8px 25px rgba(0,0,0,0.20);

}


/* =====================================================
   SECTION TITLES
   ===================================================== */

.section-title {

    font-size: 28px;

    font-weight: 750;

    margin-top: 30px;

    margin-bottom: 18px;

    color: #ffffff;

}


/* =====================================================
   INPUT LABELS
   ===================================================== */

label {

    color: #dce8f5 !important;

    font-weight: 600 !important;

}


/* =====================================================
   INPUT BOXES
   ===================================================== */

.stSelectbox > div > div {

    background:
        rgba(255,255,255,0.07) !important;

    color: white !important;

    border:
        1px solid rgba(255,255,255,0.15) !important;

    border-radius: 12px !important;

}


.stNumberInput input {

    background:
        rgba(255,255,255,0.07) !important;

    color: white !important;

    border:
        1px solid rgba(255,255,255,0.15) !important;

    border-radius: 12px !important;

}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {

    width: 100%;

    height: 58px;

    border-radius: 15px;

    border:
        1px solid rgba(255,255,255,0.18);

    background:
        linear-gradient(
            135deg,
            #00bcd4,
            #6755e8
        );

    color: white;

    font-size: 17px;

    font-weight: 700;

    box-shadow:
        0 8px 25px rgba(0,188,212,0.25);

    transition:
        all 0.3s ease;

}


.stButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 12px 30px rgba(103,85,232,0.40);

}


/* =====================================================
   METRIC CARDS
   ===================================================== */

[data-testid="stMetric"] {

    background:
        rgba(255,255,255,0.06);

    border:
        1px solid rgba(255,255,255,0.12);

    padding: 22px;

    border-radius: 18px;

    backdrop-filter: blur(15px);

}


[data-testid="stMetricValue"] {

    color: #00e5ff;

}


/* =====================================================
   PROGRESS BAR
   ===================================================== */

.stProgress > div > div > div {

    background:
        linear-gradient(
            90deg,
            #00e5ff,
            #7c4dff,
            #00ffa3
        );

}


/* =====================================================
   SIDEBAR
   ===================================================== */

section[data-testid="stSidebar"] {

    background:
        rgba(5,14,27,0.95);

    border-right:
        1px solid rgba(255,255,255,0.08);

}


/* =====================================================
   INFO BOX
   ===================================================== */

div[data-testid="stAlert"] {

    border-radius: 14px;

    background:
        rgba(0,180,255,0.08);

    border:
        1px solid rgba(0,200,255,0.15);

}


/* =====================================================
   TABLE
   ===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

}


/* =====================================================
   REMOVE STREAMLIT DEFAULT MENU
   ===================================================== */

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

    <div class="hero-title">
        ✈️ Holiday Package Purchase Predictor
    </div>

    <div class="hero-description">
        An end-to-end Machine Learning application that predicts
        whether a customer is likely to purchase a holiday package
        based on customer demographics, interaction details,
        travel behavior, and sales-pitch information.
    </div>

    <div class="hero-description">
        Enter the customer's information below and let the trained
        Random Forest Classification model generate a prediction.
    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# ABOUT PROJECT
# =========================================================

st.markdown(
    '<div class="section-title">🤖 About This Project</div>',
    unsafe_allow_html=True
)


st.markdown(
    """
<div class="glass-card">
""",
    unsafe_allow_html=True
)

st.subheader("What does this project do?")

st.write(
    """
    This project is a Holiday Package Purchase Prediction system.
    It uses customer-related information to predict whether a
    customer is likely to purchase a holiday package.
    """
)

st.subheader("🧠 Machine Learning Model")

st.write(
    """
    The prediction is performed using a Random Forest Classifier.
    Random Forest is an ensemble classification algorithm that
    combines multiple decision trees to make a final prediction.
    """
)

st.subheader("⚙️ Data Preprocessing")

st.write(
    """
    Before making a prediction, the customer input is passed through
    the same preprocessing pipeline used during model training.
    Categorical variables are handled using One-Hot Encoding and
    numerical variables are scaled using StandardScaler.
    """
)

st.subheader("🎯 Prediction Target")

st.write(
    """
    The target variable is ProdTaken.
    """
)

st.markdown(
    """
    - **0** → Customer is predicted not to purchase the package
    - **1** → Customer is predicted to purchase the package
    """
)

st.markdown(
    """
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

### 🌲 Random Forest

Ensemble machine learning algorithm based on multiple
decision trees for classification.

</div>
""",
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        """
<div class="feature-card">

### 🔄 Preprocessing

Categorical variables are One-Hot Encoded and numerical
variables are standardized before prediction.

</div>
""",
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        """
<div class="feature-card">

### 📊 Probability

The application also displays the model's estimated
probability of package purchase.

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# CUSTOMER INPUT
# =========================================================

st.markdown(
    '<div class="section-title">📝 Customer Information</div>',
    unsafe_allow_html=True
)


st.info(
    "💡 Hover over the information icon beside each input "
    "to understand what the feature represents."
)


with st.form("prediction_form"):

    col1, col2 = st.columns(2)


    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30,
            step=1,
            help="Customer's age in years."
        )


        type_of_contact = st.selectbox(
            "Type of Contact",
            [
                "Self Enquiry",
                "Company Invited"
            ],
            help="How the customer came into contact with the company."
        )


        city_tier = st.selectbox(
            "City Tier",
            [1, 2, 3],
            help="Classification/tier of the customer's city."
        )


        duration_of_pitch = st.number_input(
            "Duration of Pitch",
            min_value=0,
            value=10,
            step=1,
            help="Duration of the sales presentation given to the customer."
        )


        occupation = st.selectbox(
            "Occupation",
            [
                "Salaried",
                "Small Business",
                "Free Lancer"
            ],
            help="Customer's occupation or employment category."
        )


        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ],
            help="Customer's gender."
        )


        number_of_followups = st.number_input(
            "Number of Followups",
            min_value=0,
            value=3,
            step=1,
            help="Number of follow-up interactions with the customer."
        )


        product_pitched = st.selectbox(
            "Product Pitched",
            [
                "Basic",
                "Deluxe",
                "King",
                "Standard",
                "Super Deluxe"
            ],
            help="Holiday package/product presented to the customer."
        )


        preferred_property_star = st.selectbox(
            "Preferred Property Star",
            [3, 4, 5],
            help="Preferred hotel/property star rating."
        )


    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with col2:

        marital_status = st.selectbox(
            "Marital Status",
            [
                "Married",
                "Unmarried",
                "Single",
                "Divorced"
            ],
            help="Customer's marital status."
        )


        number_of_trips = st.number_input(
            "Number of Trips",
            min_value=0,
            value=3,
            step=1,
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
                 "1 = Lowest and 5 = Highest."
        )


        own_car = st.selectbox(
            "Own Car",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the customer owns a car. 1 = Yes, 0 = No."
        )


        designation = st.selectbox(
            "Designation",
            [
                "AVP",
                "Executive",
                "Manager",
                "Senior Manager",
                "VP"
            ],
            help="Customer's professional designation."
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
            step=1,
            help="Total number of people visiting."
        )


    st.markdown("<br>", unsafe_allow_html=True)


    submitted = st.form_submit_button(
        "🔮 Predict Holiday Package Purchase"
    )


# =========================================================
# PREDICTION
# =========================================================

if submitted:

    input_data = pd.DataFrame(
        {
            "Age": [age],

            "TypeofContact": [
                type_of_contact
            ],

            "CityTier": [
                city_tier
            ],

            "DurationOfPitch": [
                duration_of_pitch
            ],

            "Occupation": [
                occupation
            ],

            "Gender": [
                gender
            ],

            "NumberOfFollowups": [
                number_of_followups
            ],

            "ProductPitched": [
                product_pitched
            ],

            "PreferredPropertyStar": [
                preferred_property_star
            ],

            "MaritalStatus": [
                marital_status
            ],

            "NumberOfTrips": [
                number_of_trips
            ],

            "Passport": [
                passport
            ],

            "PitchSatisfactionScore": [
                pitch_satisfaction_score
            ],

            "OwnCar": [
                own_car
            ],

            "Designation": [
                designation
            ],

            "MonthlyIncome": [
                monthly_income
            ],

            "TotalVisiting": [
                total_visiting
            ]
        }
    )


    try:

        # =================================================
        # PREPROCESS INPUT
        # =================================================

        transformed_data = preprocessor.transform(
            input_data
        )


        # =================================================
        # MODEL PREDICTION
        # =================================================

        prediction = model.predict(
            transformed_data
        )[0]


        # =================================================
        # PREDICTION PROBABILITY
        # =================================================

        probability = model.predict_proba(
            transformed_data
        )[0][1]


        # =================================================
        # RESULT
        # =================================================

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


        result_col1, result_col2 = st.columns(2)


        with result_col1:

            st.metric(
                "Purchase Probability",
                f"{probability * 100:.2f}%"
            )


        with result_col2:

            st.metric(
                "Prediction",
                "Purchase"
                if prediction == 1
                else "Not Purchase"
            )


        st.progress(
            float(probability)
        )


        st.markdown(
            """
<div class="glass-card">
""",
            unsafe_allow_html=True
        )


        st.subheader("📊 Understanding the Result")


        st.write(
            f"""
            The model estimates a purchase probability of
            **{probability * 100:.2f}%** based on the customer
            information provided.
            """
        )


        st.write(
            """
            This result is generated by the trained Random Forest
            Classifier. The probability represents the model's
            prediction and should not be considered a guarantee
            of the customer's actual behavior.
            """
        )


        st.markdown(
            """
</div>
""",
            unsafe_allow_html=True
        )


    except Exception as e:

        st.error(
            "Prediction failed. Please check the input values."
        )

        st.exception(e)


# =========================================================
# INPUT GUIDE
# =========================================================

st.divider()


st.markdown(
    '<div class="section-title">📚 Input Guide</div>',
    unsafe_allow_html=True
)


input_guide = pd.DataFrame(
    {
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

            "How the customer came into contact with the company.",

            "Classification/tier of the customer's city.",

            "Duration of the sales pitch given to the customer.",

            "Customer's occupation category.",

            "Customer's gender.",

            "Number of follow-up interactions with the customer.",

            "Holiday package presented to the customer.",

            "Preferred hotel/property star rating.",

            "Customer's marital status.",

            "Number of trips taken by the customer.",

            "Whether the customer has a passport.",

            "Customer's satisfaction score for the sales pitch.",

            "Whether the customer owns a car.",

            "Customer's professional designation.",

            "Customer's monthly income.",

            "Total number of people visiting."
        ]
    }
)


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
<div style="
    text-align: center;
    color: #8191a5;
    padding: 35px;
    font-size: 14px;
">

    ✈️ <b>Holiday Package Purchase Prediction</b>

    <br><br>

    Built with Python • Pandas • Scikit-learn • Streamlit

    <br>

    Machine Learning Model:
    <b>Random Forest Classifier</b>

</div>
""",
    unsafe_allow_html=True
)
