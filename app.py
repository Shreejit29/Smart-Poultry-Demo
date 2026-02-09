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

# ---------- SESSION STATE ----------
if "role" not in st.session_state:
    st.session_state.role = None

if "orders" not in st.session_state:
    st.session_state.orders = []

# ---------- LOGIN SCREEN ----------
st.title("🐔 Smart Poultry Link")
st.caption("Investor Demo – Workflow & Governance Showcase")

if st.session_state.role is None:
    st.subheader("Login as")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("🛒 Buyer"):
            st.session_state.role = "buyer"
            st.switch_page("pages/buyer.py")

    with c2:
        if st.button("🚜 Farmer"):
            st.session_state.role = "farmer"
            st.switch_page("pages/farmer.py")

    with c3:
        if st.button("🛡️ Admin"):
            st.session_state.role = "admin"
            st.switch_page("pages/admin.py")
else:
    st.success(f"Logged in as: {st.session_state.role.upper()}")
