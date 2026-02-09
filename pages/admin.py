import streamlit as st

st.title("🛡️ Admin Control – Phase 1")

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("💰 Platform Commission Control")

commission = st.slider(
    "Set Commission Rate (%)",
    min_value=3,
    max_value=10,
    value=int(st.session_state.commission_rate * 100)
)

st.session_state.commission_rate = commission / 100

st.write(f"Current Commission Rate: **{commission}%**")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.subheader("📊 System Snapshot")
st.write("Total Buyers:", len(st.session_state.buyers))
st.write("Total Farmers:", len(st.session_state.farmers))
st.write("Total Orders:", len(st.session_state.orders))
