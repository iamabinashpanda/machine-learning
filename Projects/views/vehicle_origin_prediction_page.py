import joblib
import pandas as pd
import streamlit as st
import os

st.set_page_config(page_title="Car Country Predictor",page_icon="🏎️",layout="wide",initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    /* Card Container Styling */
    .metric-card {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
    }
    
    /* Result Box Styling */
    .result-box {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        margin-top: 10px;
    }
    .result-title {
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.85;
        margin-bottom: 5px;
    }
    .result-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    </style>
""",
    unsafe_allow_html=True,
)

@st.cache_resource
def load_artifacts(file_path):
    try:
        artifacts = joblib.load(file_path)
        return artifacts
    except Exception as e:
        st.error(f"⚠️ Failed to load model artifact from `{file_path}`: {e}")
        return None

MODEL_PATH = "models/car_country_pred_model.joblib"
artifacts = load_artifacts(MODEL_PATH)

REGION_FLAGS = {"US.": "🇺🇸", "Europe.": "🇪🇺", "Japan.": "🇯🇵"}

st.title("🏎️ Vehicle Origin Prediction")
st.caption("Utilize trained Machine Learning models to predict a vehicle's manufacturing region based on its engine and performance specifications.")
st.divider()

if artifacts:
    model = artifacts["model"]
    translator = artifacts["translator"]

    # Layout: 2 Columns (Inputs on left, Live Results/Analysis on right)
    col_input, col_output = st.columns([3, 2], gap="large")

    with col_input:
        st.subheader("🛠️ Vehicle Specifications")

        with st.form("car_spec_form"):
            # Sub-columns for clean grouping
            f_col1, f_col2 = st.columns(2)

            with f_col1:
                st.markdown("**Engine Specs**")
                cylinders = st.select_slider("Cylinders", options=[3, 4, 5, 6, 8], value=4)
                cubicinches = st.number_input("Displacement (cu. in.)",min_value=50.0,max_value=500.0,value=150.0,step=5.0,help="Engine cubic inches displacement.",)
                hp = st.slider("Horsepower (HP)",min_value=40,max_value=300,value=100,step=1,)

            with f_col2:
                st.markdown("**Performance & Age**")
                mpg = st.number_input("Miles Per Gallon (MPG)",min_value=5.0,max_value=60.0,value=22.5,step=0.5,)
                weightlbs = st.number_input("Weight (lbs)",min_value=1000,max_value=6000,value=2500,step=50,)
                time_to_60 = st.slider("0–60 mph Acceleration (sec)",min_value=5.0,max_value=30.0,value=15.0,step=0.5,                )

            year = st.selectbox("Model Year",options=list(range(1970, 1983)),index=5,help="Year of vehicle release.",            )

            submit_btn = st.form_submit_button("🔮 Predict Origin", use_container_width=True, type="primary")

    with col_output:
        st.subheader("📊 Prediction Results")

        if submit_btn:
            # Construct feature DataFrame matching exact feature names & order
            input_df = pd.DataFrame(
                [
                    {
                        "mpg": mpg,
                        "cylinders": cylinders,
                        "cubicinches": cubicinches,
                        "hp": hp,
                        "weightlbs": weightlbs,
                        "time-to-60": time_to_60,
                        "year": year,
                    }
                ]
            )

            try:
                # 1. Prediction & Probabilities
                pred_encoded = model.predict(input_df)[0]
                pred_label = translator.inverse_transform([pred_encoded])[0]

                # Fetch probabilities if decision tree supports it
                probs = (
                    model.predict_proba(input_df)[0]
                    if hasattr(model, "predict_proba")
                    else None
                )

                flag = REGION_FLAGS.get(pred_label, "🌐")

                # 2. Result Banner Display
                st.markdown(
                    f"""
                    <div class="result-box">
                        <div class="result-title">Predicted Region</div>
                        <div class="result-value">{flag} {pred_label}</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                st.write("")  # Spacing

                # 3. Probability Distribution (Bar Chart UI)
                if probs is not None:
                    st.markdown("**Prediction Confidence**")
                    classes = translator.classes_
                    prob_df = pd.DataFrame(
                        {"Region": classes, "Probability": probs}
                    ).set_index("Region")

                    st.bar_chart(prob_df, height=180)

                # 4. Feature Summary Expander
                with st.expander("🔍 Inspect Model Input Vector"):
                    st.json(input_df.to_dict(orient="records")[0])

            except Exception as err:
                st.error(f"Error executing prediction pipeline: {err}")
        else:
            st.info("👈 Fill out the specifications and click **Predict Origin** to see the result.")

else:
    st.warning("Please ensure the `.joblib` model artifact path is correct.")