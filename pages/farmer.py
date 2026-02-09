import streamlit as st
import uuid

st.title("🚜 Farmer Profile")

st.markdown("<div class='card'>", unsafe_allow_html=True)

farmer_name = st.text_input("Farmer Name")
region = st.selectbox("Region", ["Pune", "Mumbai", "Nashik", "Nagpur"])
daily_capacity = st.number_input("Daily Capacity (units)", min_value=1, value=100)
available = st.checkbox("Available Today", value=True)

if st.button("💾 Save Farmer Profile"):
    farmer_id = str(uuid.uuid4())[:8]

    st.session_state.farmers[farmer_id] = {
        "name": farmer_name,
        "region": region,
        "capacity": daily_capacity,
        "available": available
    }

    st.session_state.current_farmer = farmer_id
    st.success("Farmer profile created")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- SHOW CURRENT FARMER ----------
if "current_farmer" in st.session_state:
    st.subheader("👨‍🌾 Your Profile")
    st.json(st.session_state.farmers[st.session_state.current_farmer])
