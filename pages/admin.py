import streamlit as st

st.title("🛡️ Admin – Operations Monitor")

delayed = 0
rejected = 0

for o in st.session_state.orders.values():
    if o["status"] == "Rejected":
        rejected += 1
    if "accepted_at" in o:
        from datetime import datetime
        if (datetime.now() - o["accepted_at"]).seconds / 3600 > 4:
            delayed += 1

st.metric("Rejected Orders", rejected)
st.metric("Delayed Deliveries", delayed)

st.divider()

for oid, o in st.session_state.orders.items():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(f"Order ID: {oid}")
    st.write(f"Status: {o['status']}")
    if "rejection_reason" in o:
        st.write(f"Reason: {o['rejection_reason']}")
    st.markdown("</div>", unsafe_allow_html=True)
