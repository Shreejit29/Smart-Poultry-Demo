import streamlit as st
import uuid

st.title("🛒 Buyer Profile")

st.markdown("<div class='card'>", unsafe_allow_html=True)

buyer_name = st.text_input("Buyer Name")
buyer_type = st.selectbox("Buyer Type", ["Retailer", "Hotel", "Wholesaler"])
preferred_region = st.selectbox("Preferred Region", ["Pune", "Mumbai", "Nashik", "Nagpur"])
preferred_product = st.selectbox("Preferred Product", ["Broiler Chicken", "Eggs", "Country Chicken"])

if st.button("💾 Save Buyer Profile"):
    buyer_id = str(uuid.uuid4())[:8]

    st.session_state.buyers[buyer_id] = {
        "name": buyer_name,
        "type": buyer_type,
        "region": preferred_region,
        "product": preferred_product
    }

    st.session_state.current_buyer = buyer_id
    st.success("Buyer profile created")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- SHOW CURRENT BUYER ----------
if "current_buyer" in st.session_state:
    st.subheader("👤 Your Profile")
    st.json(st.session_state.buyers[st.session_state.current_buyer])
