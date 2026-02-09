import streamlit as st
from datetime import datetime

st.title("🚜 Farmer Dashboard")

# -------------------------------------------------
# AUTO DEMO FARMER (Smooth Demo Experience)
# -------------------------------------------------
if "current_farmer" not in st.session_state:
    demo_farmer_id = "DEMO_FARMER"
    st.session_state.farmers[demo_farmer_id] = {
        "name": "Demo Farmer",
        "region": "Pune",
        "capacity": 500,
        "available": True
    }
    st.session_state.current_farmer = demo_farmer_id

farmer_id = st.session_state.current_farmer
farmer = st.session_state.farmers[farmer_id]

st.subheader(f"Welcome, {farmer['name']} ({farmer['region']})")

# -------------------------------------------------
# ⭐ FARMER RATING (PHASE 4)
# -------------------------------------------------
ratings = [
    o["rating"]
    for o in st.session_state.orders.values()
    if o.get("farmer_id") == farmer_id and "rating" in o
]

if ratings:
    avg_rating = round(sum(ratings) / len(ratings), 2)
    st.metric("⭐ Average Rating", avg_rating)
else:
    st.metric("⭐ Average Rating", "No ratings yet")

st.divider()

# -------------------------------------------------
# 💰 EARNINGS DASHBOARD (PHASE 3)
# -------------------------------------------------
total_earnings = 0
completed_orders = 0

for o in st.session_state.orders.values():
    if o["farmer_id"] == farmer_id and o["status"] == "Delivered":
        total_earnings += o["price"]
        completed_orders += 1

c1, c2 = st.columns(2)
c1.metric("Total Earnings (₹)", total_earnings)
c2.metric("Completed Orders", completed_orders)

st.divider()

# -------------------------------------------------
# 📦 ORDER MANAGEMENT + LOGISTICS
# -------------------------------------------------
for oid, o in st.session_state.orders.items():

    if o["farmer_id"] != farmer_id:
        continue

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write(f"**Order ID:** {oid}")
    st.write(f"Product: {o['product']}")
    st.write(f"Quantity: {o['quantity']}")
    st.write(f"Order Value: ₹{o['price']}")
    st.write(f"Status: **{o['status']}**")

    # ---------- ACCEPT / REJECT ----------
    if o["status"] == "Order Placed":

        if o["quantity"] > farmer["capacity"]:
            st.error("❌ Quantity exceeds daily capacity")
        else:
            if st.button(f"✅ Accept Order {oid}", key=f"accept_{oid}"):
                st.session_state.orders[oid]["status"] = "Accepted"
                st.session_state.orders[oid]["accepted_at"] = datetime.now()
                st.success("Order accepted")

            reject_reason = st.selectbox(
                "Reject Reason",
                ["Out of stock", "Price issue", "Delay expected"],
                key=f"reject_reason_{oid}"
            )

            if st.button(f"❌ Reject Order {oid}", key=f"reject_{oid}"):
                st.session_state.orders[oid]["status"] = "Rejected"
                st.session_state.orders[oid]["rejection_reason"] = reject_reason
                st.warning("Order rejected")

    # ---------- LOGISTICS ----------
    elif o["status"] == "Accepted":
        if st.button(f"🚚 Mark In Transit {oid}", key=f"transit_{oid}"):
            st.session_state.orders[oid]["status"] = "In Transit"

    elif o["status"] == "In Transit":
        if st.button(f"📦 Mark Delivered {oid}", key=f"deliver_{oid}"):
            st.session_state.orders[oid]["status"] = "Delivered"
            st.session_state.orders[oid]["delivered_at"] = datetime.now()

    # ---------- SLA / DELAY INDICATOR ----------
    if "accepted_at" in o:
        hours_elapsed = (datetime.now() - o["accepted_at"]).seconds / 3600

        if hours_elapsed < 2:
            st.success("🟢 On Time")
        elif hours_elapsed < 4:
            st.warning("🟡 Slight Delay")
        else:
            st.error("🔴 Delayed")

    st.markdown("</div>", unsafe_allow_html=True)
