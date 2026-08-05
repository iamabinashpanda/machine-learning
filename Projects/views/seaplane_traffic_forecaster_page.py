import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="SeaPlane Traffic Forecaster",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Load Model and Data
@st.cache_resource
def load_model():
    data = joblib.load("./models/seaplane_sarimax_model.joblib")
    return data["model_results"], data["historical_data"]


try:
    results, df_hist = load_model()
    model_loaded = True
except Exception as e:
    st.error(
        f"Error loading model file `seaplane_sarimax_model.joblib`. Please ensure the file exists in the directory.\n\nDetails: {e}"
    )
    model_loaded = False

if model_loaded:
    # Sidebar Controls
    st.sidebar.header("⚙️ Forecast Settings")
    forecast_period = st.sidebar.slider(
        "Select Forecast Horizon (Months):",
        min_value=1,
        max_value=48,
        value=24,
        step=1,
    )

    show_confidence = st.sidebar.checkbox(
        "Show Confidence Interval", value=True
    )
    history_window = st.sidebar.selectbox(
        "Historical Context Window:",
        ["All Data", "Last 3 Years", "Last 5 Years"],
        index=0,
    )

    # Filter Historical Data View
    if history_window == "Last 3 Years":
        plot_hist = df_hist.iloc[-36:]
    elif history_window == "Last 5 Years":
        plot_hist = df_hist.iloc[-60:]
    else:
        plot_hist = df_hist

    # Generate Forecast
    forecast_obj = results.get_forecast(steps=forecast_period)
    forecast_log = forecast_obj.predicted_mean
    conf_int_log = forecast_obj.conf_int()

    # Revert Log Transformation
    forecast_val = np.exp(forecast_log)
    conf_int_val = np.exp(conf_int_log)

    forecast_df = pd.DataFrame(
        {
            "Forecasted Passengers": np.round(forecast_val).astype(int),
            "Lower Bound": np.round(conf_int_val.iloc[:, 0]).astype(int),
            "Upper Bound": np.round(conf_int_val.iloc[:, 1]).astype(int),
        },
        index=forecast_val.index,
    )

    # Header UI
    st.title("✈️ SeaPlane Passenger Traffic Forecasting")
    st.caption(
        "Time-series predictive modeling using SARIMAX (1, 1, 1) x (0, 1, 0, 12)"
    )
    st.markdown("---")

    # Metric Cards
    m1, m2, m3, m4 = st.columns(4)
    avg_hist = int(df_hist.iloc[:, 0].mean())
    total_forecast = int(forecast_df["Forecasted Passengers"].sum())
    avg_forecast = int(forecast_df["Forecasted Passengers"].mean())
    peak_month = forecast_df["Forecasted Passengers"].idxmax().strftime("%B %Y")

    m1.metric("Historical Avg / Month", f"{avg_hist:,}")
    m2.metric("Projected Total Demand", f"{total_forecast:,}")
    m3.metric("Projected Monthly Avg", f"{avg_forecast:,}")
    m4.metric("Peak Demand Month", peak_month)

    st.markdown("---")

    # Main Chart Visualization (Plotly Interactive)
    fig = go.Figure()

    # Historical Line
    fig.add_trace(
        go.Scatter(
            x=plot_hist.index,
            y=plot_hist.iloc[:, 0],
            mode="lines",
            name="Historical Traffic",
            line=dict(color="#1f77b4", width=2.5),
        )
    )

    # Confidence Interval Shading
    if show_confidence:
        fig.add_trace(
            go.Scatter(
                x=list(forecast_df.index) + list(forecast_df.index[::-1]),
                y=list(forecast_df["Upper Bound"])
                + list(forecast_df["Lower Bound"][::-1]),
                fill="toself",
                fillcolor="rgba(255, 127, 14, 0.2)",
                line=dict(color="rgba(255,255,255,0)"),
                hoverinfo="skip",
                name="95% Confidence Interval",
            )
        )

    # Forecast Line
    fig.add_trace(
        go.Scatter(
            x=forecast_df.index,
            y=forecast_df["Forecasted Passengers"],
            mode="lines+markers",
            name="SARIMAX Forecast",
            line=dict(color="#ff7f0e", width=3, dash="dash"),
        )
    )

    fig.update_layout(
        title=f"Passenger Traffic Forecast ({forecast_period} Months)",
        xaxis_title="Date",
        yaxis_title="Number of Passengers",
        hovermode="x unified",
        template="plotly_white",
        height=500,
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
        ),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Data Table & Export Section
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📊 Forecast Table")
        st.dataframe(forecast_df, use_container_width=True)

    with col_right:
        st.subheader("📥 Export Results")
        csv_data = forecast_df.to_csv().encode("utf-8")
        st.download_button(
            label="Download Forecast CSV",
            data=csv_data,
            file_name=f"seaplane_forecast_{forecast_period}_months.csv",
            mime="text/csv",
            use_container_width=True,
        )