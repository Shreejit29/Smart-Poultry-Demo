import streamlit as st
import pandas as pd

st.title("🛡️ Admin Intelligence Center")

orders = st.session_state.orders

# ---------- EMPTY STATE ----------
if not orders:
    st.info("No orders yet")
    st.stop()

# ---------- BUILD DATAFRAME ----------
df = pd.DataFrame.from_dict(orders, orient="index")

# ---------- GUARANTEE REQUIRED COLUMNS ----------
required_columns = {
    "total": 0,
    "quantity": 0,
    "commission": 0,
    "rating": None,
    "status": "Unknown"
}

for col, default in required_columns.items():
    if col not in df.columns:
        df[col] = default

# ---------- KPIs ----------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Orders", len(df))
c2.metric("Total Revenue (₹)", int(df["total"].sum()))
c3.metric("Total Commission (₹)", int(df["commission"].sum()))
c4.metric("Delivered Orders", len(df[df["status"] == "Delivered"]))

st.divider()

# ---------- REGION ANALYTICS ----------
buyer_regions = {
    oid: st.session_state.buyers[o["buyer_id"]]["region"]
    for oid, o in orders.items()
    if o["buyer_id"] in st.session_state.buyers
}

df["region"] = pd.Series(buyer_regions)

st.subheader("🌍 Region-wise Revenue")
st.bar_chart(df.groupby("region")["total"].sum())

st.divider()

# ---------- FARMER PERFORMANCE (FIXED) ----------
st.subheader("👨‍🌾 Farmer Performance")

farmer_perf = (
    df.groupby("farmer_id", dropna=False)
      .agg(
          Revenue=("total", "sum"),
          Units_Sold=("quantity", "sum"),
          Avg_Rating=("rating", "mean")
      )
      .fillna(0)
)

st.dataframe(farmer_perf)

st.divider()

# ---------- WHAT-IF COMMISSION SIMULATION ----------
st.subheader("📈 What-if Commission Simulation")

sim_rate = st.slider("Simulate Commission (%)", 3, 10, 7)

projected_commission = int(df["total"].sum() * (sim_rate / 100))
st.write(f"Projected Commission at {sim_rate}%: ₹{projected_commission}")

st.divider()

# ---------- EXCEPTION DASHBOARD ----------
st.subheader("🚨 Exceptions")

c1, c2 = st.columns(2)
c1.metric("Rejected Orders", len(df[df["status"] == "Rejected"]))
c2.metric("In Transit Orders", len(df[df["status"] == "In Transit"]))

st.divider()

# ---------- RESET ----------
if st.button("🔄 RESET DEMO"):
    st.session_state.orders = {}
    st.session_state.buyers = {}
    st.session_state.farmers = {}
    st.success("Demo reset successfully")
