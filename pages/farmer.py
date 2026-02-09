import streamlit as st

st.title("🚜 Farmer Dashboard")

if not st.session_state.orders:
    st.info("No orders yet")
else:
    for i, o in enumerate(st.session_state.orders):
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.write(f"**Product:** {o['product']}")
        st.write(f"**Buyer:** {o['buyer']}")
        st.write(f"**Region:** {o['region']}")
        st.write(f"**Quantity:** {o['quantity']}")
        st.write(f"**Status:** {o['status']}")

        if o["status"] == "Paid":
            if st.button(f"🚚 Assign Delivery #{i+1}"):
                st.session_state.orders[i]["status"] = "In Transit"

        elif o["status"] == "In Transit":
            if st.button(f"📦 Mark Delivered #{i+1}"):
                st.session_state.orders[i]["status"] = "Delivered"

        st.markdown("</div>", unsafe_allow_html=True)
