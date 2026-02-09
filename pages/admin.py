import streamlit as st
import pandas as pd

st.title("🛡️ Admin Control Center")

df = pd.DataFrame(st.session_state.orders)

# ---------- KPI ----------
c1, c2, c3 = st.columns(3)
c1.metric("Total Orders", len(df))
c2.metric("Total Revenue (₹)", int(df.amount.sum()) if not df.empty else 0)
c3.metric("Platform Commission (₹)", int(df.commission.sum()) if not df.empty else 0)

st.divider()

# ---------- STATUS ----------
if not df.empty:
    st.subheader("📊 Orders by Status")
    st.bar_chart(df["status"].value_counts())

# ---------- REGION ----------
if not df.empty:
    st.subheader("🌍 Region-wise Revenue")
    st.bar_chart(df.groupby("region")["amount"].sum())

# ---------- FARMER PERFORMANCE ----------
if not df.empty:
    st.subheader("👨‍🌾 Farmer Performance")
    farmer_perf = df.groupby("farmer").agg({
        "amount": "sum",
        "quantity": "sum"
    })
    st.dataframe(farmer_perf)

st.divider()

# ---------- RESET ----------
if st.button("🔄 Reset Demo"):
    st.session_state.orders = []
    st.success("Demo reset successfully")
