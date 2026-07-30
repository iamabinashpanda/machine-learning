import streamlit as st
import joblib

# 1. Page Configuration
st.set_page_config(
    page_title="Purchase Predictor AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Modern Light Mode & Transparent Gradient Styling
st.markdown("""
<style>
    /* Light Mode Background with Soft Gradient */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 50%, #e2e8f0 100%);
        color: #0f172a;
    }

    /* Glassmorphic White Header Card */
    .header-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(226, 232, 240, 0.8);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-bottom: 2rem;
    }

    .header-card h1 {
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
    }

    .header-card p {
        color: #64748b;
        font-size: 1.1rem;
        margin: 0;
    }

    /* Form Container Card */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.03);
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

    /* Soft Transparent Result Cards */
    .result-yes {
        background: linear-gradient(135deg, rgba(237, 247, 242, 0.9) 0%, rgba(209, 250, 229, 0.8) 100%);
        backdrop-filter: blur(8px);
        border: 1px solid #a7f3d0;
        color: #065f46;
        padding: 1.75rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 20px -5px rgba(16, 185, 129, 0.1);
        animation: fadeIn 0.4s ease-out;
    }

    .result-no {
        background: linear-gradient(135deg, rgba(254, 242, 242, 0.9) 0%, rgba(254, 226, 226, 0.8) 100%);
        backdrop-filter: blur(8px);
        border: 1px solid #fecaca;
        color: #991b1b;
        padding: 1.75rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 20px -5px rgba(239, 68, 68, 0.1);
        animation: fadeIn 0.4s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# 3. Model Loader
@st.cache_resource
def load_model():
    return joblib.load("models/logistic_regression_model.joblib")

# 4. Header Section
st.markdown("""
<div class="header-card">
    <h1>Client Purchase Predictor</h1>
    <p>Predict whether a client will complete a purchase based on demographic and salary metrics.</p>
</div>
""", unsafe_allow_html=True)

# 5. Interactive Form Section
with st.form("prediction_form", clear_on_submit=False):
    st.markdown("##### 👤 **Client Attributes**")
    
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        age = st.slider("Age", min_value=18, max_value=100, value=30, help="Select customer age")

    with col2:
        gender = st.radio("Gender", options=["Male", "Female"], horizontal=True)

    with col3:
        expected_salary = st.slider(
            "Expected Salary ($)", 
            min_value=0, 
            max_value=150000, 
            value=45000, 
            step=1000, 
            format="$%d"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 6. Action Button
    submit_button = st.form_submit_button("🚀 Run Prediction Model", use_container_width=True)

# 7. Prediction Results
if submit_button:
    try:
        logistic_regressionmodel = load_model()
        
        is_male = 1 if gender == "Male" else 0
        features = [[is_male, age, expected_salary]]
        
        prediction = logistic_regressionmodel.predict(features)
        has_purchased = prediction[0] == 1

        st.markdown("<br>", unsafe_allow_html=True)
        
        if has_purchased:
            st.markdown("""
            <div class="result-yes">
                <span style="font-size: 0.85rem; letter-spacing: 1.5px; font-weight: 700; text-transform: uppercase;">Prediction Output</span>
                <h2 style="margin: 0.4rem 0 0 0; color: #047857; font-size: 2rem; font-weight: 800;">Purchased: YES ✅</h2>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-no">
                <span style="font-size: 0.85rem; letter-spacing: 1.5px; font-weight: 700; text-transform: uppercase;">Prediction Output</span>
                <h2 style="margin: 0.4rem 0 0 0; color: #b91c1c; font-size: 2rem; font-weight: 800;">Purchased: NO ❌</h2>
            </div>
            """, unsafe_allow_html=True)

        # Show Probability gauge if model supports it
        if hasattr(logistic_regressionmodel, "predict_proba"):
            probabilities = logistic_regressionmodel.predict_proba(features)[0]
            buy_prob = probabilities[1] * 100
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.write(f"**Model Confidence:** {buy_prob:.1f}% probability to purchase")
            st.progress(int(buy_prob))

    except Exception as e:
        st.error(f"⚠️ Unable to execute prediction: {e}")