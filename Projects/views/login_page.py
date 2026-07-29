import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

# 2. Polished CSS for Modern Card
st.markdown("""
<style>
    /* Global Page Styling */
    .stApp {
        background-color: #F1F5F9 !important;
    }

    /* Outer Wrapper Card */
    .login-card-wrapper {
        background: #FFFFFF;
        border-radius: 20px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.08);
        overflow: hidden;
        margin: 2rem auto;
        max-width: 950px;
    }

    /* LEFT PANEL - Image & Testimonial Styling */
    .left-panel {
        background: linear-gradient(rgba(15, 23, 42, 0.45), rgba(15, 23, 42, 0.75)), 
                    url('https://b2161880.smushcdn.com/2161880/wp-content/uploads/2017/09/Fotolia_165428801_Subscription_Monthly_M.jpg?lossy=1&strip=1&webp=1');
        background-size: cover;
        background-position: center;
        padding: 2.5rem;
        height: 100%;
        min-height: 520px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        color: #FFFFFF;
        border-top-left-radius: 20px;
        border-bottom-left-radius: 20px;
    }

    .brand-logo {
        font-weight: 700;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .quote {
        font-size: 1.2rem;
        font-weight: 600;
        line-height: 1.4;
        margin-bottom: 0.8rem;
    }

    .author {
        font-weight: 700;
        font-size: 0.95rem;
    }

    .author-title {
        font-size: 0.8rem;
        color: #CBD5E1;
    }

    /* RIGHT PANEL - Form Headers */
    .form-header {
        font-family: 'Georgia', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #0F172A;
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 0.4rem;
    }

    .form-sub {
        font-size: 0.85rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 1.5rem;
        line-height: 1.4;
    }

    /* Input Fields & Buttons Overrides */
    .stTextInput>div>div>input {
        border-radius: 8px !important;
        border: 1px solid #CBD5E1 !important;
        padding: 0.5rem 0.8rem !important;
        background-color: #F8FAFC !important;
    }

    .stButton>button {
        width: 100%;
        background: #0070F3 !important;
        color: #FFFFFF !important;
        border-radius: 25px !important;
        padding: 0.6rem 1rem !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        border: none !important;
    }

    .stButton>button:hover {
        background: #0051C7 !important;
    }

    /* Google Button */
    .google-btn {
        width: 100%;
        border: 1px solid #E2E8F0;
        border-radius: 25px;
        padding: 0.55rem;
        background: #FFFFFF;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        font-size: 0.9rem;
        font-weight: 600;
        color: #334155;
        cursor: pointer;
        margin-top: 0.8rem;
    }

    /* Divider */
    .divider {
        display: flex;
        align-items: center;
        text-align: center;
        color: #94A3B8;
        font-size: 0.8rem;
        margin: 1rem 0;
    }
    .divider::before, .divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #E2E8F0;
    }
    .divider::before { margin-right: .5em; }
    .divider::after { margin-left: .5em; }

    .signup-text {
        text-align: center;
        font-size: 0.82rem;
        color: #64748B;
        margin-top: 1rem;
    }
    .signup-text a {
        color: #2563EB;
        text-decoration: none;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# 3. Outer Container Setup (Centered Layout)
_, center_col, _ = st.columns([1, 10, 1])

with center_col:
    # Wrap entire grid inside the white card
    st.markdown('<div class="login-card-wrapper">', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1.1])

    # --- LEFT SIDE (Image + Quote) ---
    with col_left:
        st.markdown("""
        <div class="left-panel">
            <div class="brand-logo">⚡ ML Suite</div>
            <div>
                <div class="quote">“The perfect toolkit for all my machine learning projects.”</div>
                <div class="author">Abinash Panda</div>
                <div class="author-title">Machine Learning Enthusiast</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- RIGHT SIDE (Form & Social Login) ---
    with col_right:
        # Wrap right padding cleanly inside a sub-container
        with st.container():
            st.markdown('<div style="padding: 1.5rem 2rem 2rem 1.5rem;">', unsafe_allow_html=True)
            
            st.markdown('<div class="form-header"><br>LOGIN</div>', unsafe_allow_html=True)
            st.markdown('<div class="form-sub">We\'re glad to have you back. Enter your credentials to continue your ML journey.</div>', unsafe_allow_html=True)

            with st.form("login_form", clear_on_submit=False):
                username = st.text_input("Email / Username", placeholder="ak.sanan@gmail.com")
                password = st.text_input("Password", type="password", placeholder="••••••••")
                
                submit = st.form_submit_button("Login", use_container_width=True)

                if submit:
                    if username and password:
                        st.session_state["authenticated"] = True
                        st.session_state["user_name"] = username.split("@")[0].title()
                        st.success("Redirecting...")
                        st.rerun()
                    else:
                        st.error("Please fill in all fields.")

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)