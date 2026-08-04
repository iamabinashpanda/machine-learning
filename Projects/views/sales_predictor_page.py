import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Sales Prediction Dashboard", page_icon="📈", layout="wide"
)

st.title("📈 Advertising Sales Prediction Dashboard")
st.write("Adjust the advertising budgets to predict total sales.")

st.markdown("""
<style>
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
</style>
""",unsafe_allow_html=True)

# Load the pre-trained joblib model
@st.cache_resource
def load_model():
    return joblib.load("./models/sales_model.pkl")


model = load_model()

# --- Sidebar Inputs ---
st.sidebar.header("📊 Advertising Budgets ($)")

tv_budget = st.sidebar.slider(
    "TV Advertising", min_value=0.0, max_value=300.0, value=150.0, step=0.5
)
radio_budget = st.sidebar.slider(
    "Radio Advertising", min_value=0.0, max_value=100.0, value=25.0, step=0.5
)
newspaper_budget = st.sidebar.slider(
    "Newspaper Advertising", min_value=0.0, max_value=100.0, value=20.0, step=0.5
)

# --- Predict Sales ---
input_data = pd.DataFrame(
    [[tv_budget, radio_budget, newspaper_budget]],
    columns=["TV", "Radio", "Newspaper"],
)

predicted_sales = model.predict(input_data)[0]

# --- UI Layout ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Predicted Output")
    # Metric Card display
    st.metric(
        label="Estimated Sales Units",
        value=f"{predicted_sales:.2f} k",
        delta=f"{(predicted_sales - 10):.2f} vs Baseline",
    )

    st.markdown("---")
    st.subheader("Selected Inputs")
    st.write(f"**TV:** ${tv_budget:,.2f}")
    st.write(f"**Radio:** ${radio_budget:,.2f}")
    st.write(f"**Newspaper:** ${newspaper_budget:,.2f}")

with col2:
    st.subheader("Feature Spending Distribution")

    # Bar chart for spending breakdown
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ["TV", "Radio", "Newspaper"]
    budgets = [tv_budget, radio_budget, newspaper_budget]
    colors = ["#4C72B0", "#55A868", "#C44E52"]

    ax.bar(categories, budgets, color=colors)
    ax.set_ylabel("Budget ($)")
    ax.set_title("Current Advertising Spend")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    st.pyplot(fig)