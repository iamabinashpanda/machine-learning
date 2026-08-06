import streamlit as st

# 1. Configuration
st.set_page_config(
    page_title="ML Suite - Blue Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State Initialization for Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 3. Custom Sidebar & Menu Styling
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E3A8A 60%, #1E40AF 100%) !important;
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }
    .brand-header-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 14px;
        padding: 1.25rem 1rem;
        margin: 0.5rem 0 1.5rem 0;
    }
    .brand-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF !important;
    }
    .brand-subtitle {
        font-size: 0.78rem;
        color: #93C5FD !important;
    }
    .status-badge {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 4px;
    }
    .status-online { background-color: #4ADE80; box-shadow: 0 0 8px #4ADE80; }
    .status-offline { background-color: #F87171; box-shadow: 0 0 8px #F87171; }
</style>
""", unsafe_allow_html=True)

# 4. Sidebar Profile Header & Logout Action
with st.sidebar:
    user_status = "status-online" if st.session_state["authenticated"] else "status-offline"
    user_label = st.session_state.get("user_name", "Guest User")
    role_label = "Machine Learning Enthusiast" if st.session_state["authenticated"] else "Please Sign In"

    # Logo with Title
    st.logo(
        image="https://img.icons8.com/fluency/96/3b82f6/artificial-intelligence.png",
        icon_image="https://img.icons8.com/fluency/48/3b82f6/artificial-intelligence.png",
        link="https://github.com/iamabinashpanda"
    )

    st.markdown(f"""
        <div class="brand-header-card">
            <div class="brand-title">{user_label}</div>
            <div class="brand-subtitle">
                <span class="status-badge {user_status}"></span> {role_label}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Show Logout Button if Logged In
    if st.session_state["authenticated"]:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["user_name"] = None
            st.rerun()

# 5. Define All Pages
login_page = st.Page("views/login_page.py", title="Sign In", icon=":material/lock:")
home_page = st.Page("views/home.py", title="Overview & Home", icon=":material/home:", default=True)
car_price_page = st.Page("views/car_price_page.py", title="Car Price Predictor", icon=":material/directions_car:")
sales_page = st.Page("views/sales_predictor_page.py", title="Sales Predictor", icon=":material/analytics:")
client_page = st.Page("views/client_purchase_page.py", title="Client Purchase Predictor", icon=":material/shopping_cart:")
vehicle_origin_prediction_page = st.Page("views/vehicle_origin_prediction_page.py", title="Vehicle Origin Prediction", icon=":material/flag:")
seaplane_traffic_forecaster_page = st.Page("views/seaplane_traffic_forecaster_page.py", title="SeaPlane Traffic Forecaster", icon=":material/flight_takeoff:")

# 6. Dynamic Routing based on Authentication
if not st.session_state["authenticated"]:
    # Unauthenticated user: Show ONLY the Login page
    navigation_menu = st.navigation({"Account": [login_page]}, position="sidebar")
else:
    # Authenticated user: Unlock full application suite
    navigation_menu = st.navigation(
        {
            "General": [home_page],
            "Machine Learning Models": [car_price_page, sales_page, client_page, vehicle_origin_prediction_page,seaplane_traffic_forecaster_page]
        },
        position="sidebar"
    )

navigation_menu.run()