import streamlit as st

st.set_page_config(initial_sidebar_state="expanded")
# Custom Hero & Card CSS
st.markdown("""
<style>
    /* Hero Banner Styling */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #2563EB 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #93C5FD;
        font-weight: 400;
        max-width: 650px;
        line-height: 1.6;
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
            
    /* Metric/Feature Cards */
    .feature-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.5rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
        height: 100%;
    }
    .feature-card:hover {
        border-color: #3B82F6;
        transform: translateY(-3px);
    }
    .card-icon {
        font-size: 2rem;
        margin-bottom: 0.75rem;
        display: inline-block;
    }
    .card-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.5rem;
    }
    .card-desc {
        font-size: 0.88rem;
        color: #94A3B8;
        line-height: 1.5;
    }

    /* Badge Pills */
    .tech-badge {
        background: rgba(59, 130, 246, 0.15);
        color: #60A5FA;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(96, 165, 250, 0.3);
        display: inline-block;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">⚡ ML Suite - Blue Edition</div>
    <div class="hero-subtitle">
        Welcome to your interactive Machine Learning hub! Explore predictive analytics engines, financial forecasting tools, and classification models powered by custom trained ML pipelines.
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Key Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Active Models", value="3 Models", delta="Regression & Classif.")
with col2:
    st.metric(label="Primary Tech", value="Scikit-Learn", delta="Python 3.11")
with col3:
    st.metric(label="UI Framework", value="Streamlit", delta="v1.30+")
with col4:
    st.metric(label="System Status", value="Operational", delta="100% Ready")

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🚀 Available Applications")

# 3. Interactive App Cards
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""
    <div class="feature-card">
        <div class="card-icon">🚗</div>
        <div class="card-title">Car Price Predictor</div>
        <div class="card-desc">
            Estimate market valuations for used vehicles based on mileage, year, fuel type, and brand history using regression models.
        </div>
        <span class="tech-badge">Regression Engine</span>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="feature-card">
        <div class="card-icon">📈</div>
        <div class="card-title">Sales Predictor</div>
        <div class="card-desc">
            Forecast business revenues and product sales volumes by analyzing advertising spend across TV, Radio, and Digital channels.
        </div>
        <span class="tech-badge">Financial Forecasting</span>
    </div>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown("""
    <div class="feature-card">
        <div class="card-icon">🎯</div>
        <div class="card-title">Client Purchase Predictor</div>
        <div class="card-desc">
            Classify customer purchase intent using demographic metrics and behavior indicators to target ad campaigns effectively.
        </div>
        <span class="tech-badge">Classification Model</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Quick Navigation Tip
st.info("👈 **Get Started:** Select any model from the sidebar navigation menu on the left to begin experimenting with real-time predictions!")