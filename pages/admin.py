import streamlit as st

st.title("🛡️ Admin – Orders Overview")

for oid, o in st.session_state.orders.items():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(f"Order ID: {oid}")
    st.write(f"Buyer ID: {o['buyer_id']}")
    st.write(f"Farmer ID: {o['farmer_id']}")
    st.write(f"Total Amount: ₹{o['total']}")
    st.write(f"Commission: ₹{o['commission']}")
    st.write(f"Status: {o['status']}")
    st.markdown("</div>", unsafe_allow_html=True)
