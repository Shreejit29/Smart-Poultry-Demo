import streamlit as st
import pandas as pd

st.title("🛡️ Admin Intelligence Center")

orders = st.session_state.orders
df = pd.DataFrame.from_dict(orders, orient="index")

# ---------- KPIs ----------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Orders", len(df))
c2.metric("Total Revenue (₹)", int(df["total"].sum()) if not df.empty else 0)
c3.metric("Total Commission (₹)", int(df["commission"].sum()) if not df.empty else 0)
c4.metric("Delivered Orders", len(df[df["status"] == "Delivered"]) if not df.empty else 0)

st.divider()

# ---------- REGION ANALYTICS ----------
if not df.empty:
    st.subheader("🌍 Region-wise Revenue")
    buyer_regions = {
        oid: st.session_state.buyers[o["buyer_id"]]["region"]
        for oid, o in orders.items()
    }
    df["region"] = pd.Series(buyer_regions)
    st.bar_chart(df.groupby("region")["total"].sum())

# ---------- FARMER PERFORMANCE ----------
if not df.empty:
    st.subheader("👨‍🌾 Farmer Performance")

    farmer_perf = df.groupby("farmer_id").agg({
        "total": "sum",
        "quantity": "sum",
        "rating": "mean"
    }).fillna(0)

    farmer_perf.rename(columns={
        "total": "Revenue",
        "quantity": "Units Sold",
        "rating": "Avg Rating"
    }, inplace=True)

    st.dataframe(farmer_perf)

st.divider()

# ---------- WHAT-IF COMMISSION SIMULATION ----------
st.subheader("📈 What-if Commission Simulation")

sim_rate = st.slider("Simulate Commission (%)", 3, 10, 7)
if not df.empty:
    simulated_commission = int(df["price"].sum() * (sim_rate / 100))
    st.write(f"Projected Commission at {sim_rate}%: ₹{simulated_commission}")

st.divider()

# ---------- EXCEPTIONS ----------
st.subheader("🚨 Exception Dashboard")

rejected = len(df[df["status"] == "Rejected"]) if not df.empty else 0
delayed = len(df[df["status"] == "In Transit"]) if not df.empty else 0

c1, c2 = st.columns(2)
c1.metric("Rejected Orders", rejected)
c2.metric("Potential Delays", delayed)

st.divider()

# ---------- RESET DEMO ----------
if st.button("🔄 RESET FULL DEMO"):
    st.session_state.orders = {}
    st.session_state.buyers = {}
    st.session_state.farmers = {}
    st.success("Demo reset successfully")
