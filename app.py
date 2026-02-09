import streamlit as st

st.set_page_config(page_title="Smart Poultry Link", layout="wide")

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
.main { background-color: #f5f7fb; }
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE INITIALIZATION ----------
if "role" not in st.session_state:
    st.session_state.role = None

if "commission_rate" not in st.session_state:
    st.session_state.commission_rate = 0.05  # 5%

if "buyers" not in st.session_state:
    st.session_state.buyers = {}

if "farmers" not in st.session_state:
    st.session_state.farmers = {}

if "orders" not in st.session_state:
    st.session_state.orders = {}

# ---------- LOGIN ----------
st.title("🐔 Smart Poultry Link")
st.caption("Phase 1 – Foundation Demo")

if st.session_state.role is None:
    st.subheader("Login as")
    c1, c2, c3 = st.columns(3)

    if c1.button("🛒 Buyer"):
        st.session_state.role = "buyer"
        st.switch_page("pages/buyer.py")

    if c2.button("🚜 Farmer"):
        st.session_state.role = "farmer"
        st.switch_page("pages/farmer.py")

    if c3.button("🛡️ Admin"):
        st.session_state.role = "admin"
        st.switch_page("pages/admin.py")
