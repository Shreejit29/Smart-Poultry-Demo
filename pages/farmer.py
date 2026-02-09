import streamlit as st

st.title("🚜 Farmer Dashboard")

if "current_farmer" not in st.session_state:
    st.warning("Create Farmer Profile first (Phase 1)")
    st.stop()

farmer_id = st.session_state.current_farmer
farmer = st.session_state.farmers[farmer_id]

st.subheader(f"Welcome, {farmer['name']} ({farmer['region']})")

st.divider()

for oid, o in st.session_state.orders.items():
    if o["farmer_id"] == farmer_id:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.write(f"**Order ID:** {oid}")
        st.write(f"Product: {o['product']}")
        st.write(f"Quantity: {o['quantity']}")
        st.write(f"Total Value: ₹{o['total']}")
        st.write(f"Status: {o['status']}")

        st.markdown("</div>", unsafe_allow_html=True)
