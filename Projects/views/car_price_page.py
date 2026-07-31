import datetime
import joblib
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# 1. Page Configuration & Custom CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ValuatAuto - Car Price Predictor",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown(
    """
    <style>
    /* Global Styles */
    .main {
        padding-top: 1rem;
    }
    
    /* Header Styling */
    .title-text {
        font-size: 2.3rem !important;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8F8F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .subtitle-text {
        color: #808495;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    
    /* Input Container Cards */
    div[data-testid="stVerticalBlock"] > div:has(div.card-header) {
        background-color: rgba(151, 166, 195, 0.08);
        padding: 1.25rem 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(151, 166, 195, 0.15);
    }
    .card-header {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Price Output Box Styling */
    .metric-container {
        background: linear-gradient(135deg, #1E2640 0%, #0E1117 100%);
        border: 2px solid #FF4B4B;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    
    /* Modern Minimalist Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: #ffffff;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        border: none;
        transition: all 0.25s ease;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.35);
        color: #ffffff;
    }

    .metric-label {
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #A3ADC2;
        margin-bottom: 0.25rem;
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 800;
        color: #4DEEEA;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# 2. Model & Data Loading
# -----------------------------------------------------------------------------
@st.cache_resource
def load_bundle():
    return joblib.load("./models/car_price_model.joblib")


try:
    bundle = load_bundle()
    model = bundle["model"]
    mapping = bundle["mapping"]
    available_cities = bundle.get(
        "cities", ["Mumbai", "Thane", "Delhi", "Bangalore", "Pune"]
    )
except Exception as e:
    st.error(f"❌ Failed to load model bundle from path. Error: {e}")
    st.stop()

# -----------------------------------------------------------------------------
# 3. Sidebar Features
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image(
        "https://img.icons8.com/isometric-line/100/4a90e2/car.png", width=80
    )
    st.title("About ValuatAuto")
    st.info(
        """
        This Valuation Engine uses a **Random Forest Regressor** machine learning model trained on market price trends across major Indian cities.
        """
    )
    st.markdown("---")
    st.caption("⚙️ Model Architecture: **Scikit-Learn Pipeline**")
    st.caption("📦 Serialization: **Joblib Bundle**")

# -----------------------------------------------------------------------------
# 4. Header Section
# -----------------------------------------------------------------------------
st.markdown(
    '<p class="title-text">ValuatAuto Price Estimator</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle-text">Configure your vehicle metrics below to receive a real-time ML market valuation.</p>',
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 5. UI Layout - Feature Input Sections
# -----------------------------------------------------------------------------
col1, col2 = st.columns(2, gap="medium")

# --- Column 1: Identity & Categorical Specifications ---
with col1:
    st.markdown(
        '<div class="card-header">🚘 Vehicle Identity</div>',
        unsafe_allow_html=True,
    )

    brand_list = sorted(list(mapping.keys()))
    selected_brand = st.selectbox("Car Brand", brand_list, index=0)

    # Filtered Model Options
    available_models = sorted(list(mapping[selected_brand].keys()))
    selected_model = st.selectbox("Model Name", available_models, index=0)

    # Filtered Fuel Type Options
    available_fuels = mapping[selected_brand][selected_model]
    selected_fuel = st.selectbox("Fuel Type", available_fuels, index=0)

    selected_city = st.selectbox("City Location", sorted(available_cities))

# --- Column 2: Usage & Numerical Metrics ---
with col2:
    st.markdown(
        '<div class="card-header">📊 Condition & Usage</div>',
        unsafe_allow_html=True,
    )

    current_year = datetime.datetime.now().year
    year = st.number_input(
        "Manufacturing Year",
        min_value=2000,
        max_value=current_year,
        value=2018,
    )

    distance_travelled = st.number_input(
        "Distance Travelled (KMs)",
        min_value=0,
        value=35000,
        step=2500,
        help="Total kilometers logged on the odometer",
    )

    brand_rank = st.slider(
        "Brand Prestige Rank",
        min_value=1,
        max_value=30,
        value=5,
        help="Lower rank values represent higher market positioning/luxury brands.",
    )

    # Auto-calculate car age based on current year to keep UX frictionless
    calculated_age = max(0.0, float(current_year - year))
    car_age = st.number_input(
        "Car Age (Years)",
        min_value=0.0,
        value=calculated_age,
        help="Automatically calculated from the manufacturing year.",
    )

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. Prediction Engine & Display Output
# -----------------------------------------------------------------------------
if st.button("⚡ Calculate Estimated Valuation", use_container_width=True):
    # Construct input dataframe matching exact model feature schemas
    input_df = pd.DataFrame(
        [
            {
                "year": year,
                "brand": selected_brand,
                "model_name": selected_model,
                "distance_travelled(kms)": distance_travelled,
                "fuel_type": selected_fuel,
                "city": selected_city,
                "brand_rank": brand_rank,
                "car_age": car_age,
            }
        ]
    )

    try:
        with st.spinner("Analyzing market prices..."):
            prediction = model.predict(input_df)[0]

        st.markdown("<br>", unsafe_allow_html=True)

        # High-Impact Result Card
        st.markdown(
            f"""
            <div class="metric-container">
                <div class="metric-label">Estimated Market Price</div>
                <div class="metric-value">₹ {prediction:,.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.balloons()

    except Exception as e:
        st.error(f"Prediction Pipeline Error: {e}")