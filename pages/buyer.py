import streamlit as st
import uuid
from datetime import datetime

st.title("🛒 Buyer Dashboard")

# -------- Ensure buyer exists --------
if "current_buyer" not in st.session_state:
    st.warning("Please create Buyer Profile first (Phase 1)")
    st.stop()

buyer_id = st.session_state.current_buyer
buyer = st.session_state.buyers[buyer_id]

st.subheader(f"Welcome, {buyer['name']} ({buyer['type']})")

# -------- Select product --------
product = st.selectbox(
    "Select Product",
    ["Broiler Chicken", "Eggs", "Country Chicken"],
    index=["Broiler Chicken", "Eggs", "Country Chicken"].index(buyer["product"])
)

quantity = st.number_input("Quantity", min_value=1, value=10)

# -------- Price Logic (Demo) --------
price_map = {
    "Broiler Chicken": 120,
    "Eggs": 6,
    "Country Chicken": 180
}

unit_price = price_map[product]
base_price = unit_price * quantity
logistics_fee = 50
commission = int(base_price * st.session_state.commission_rate)
total = base_price + logistics_fee + commission

# -------- Price Breakdown Card --------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.write("### 💰 Price Breakdown")
st.write(f"Product Price: ₹{base_price}")
st.write(f"Logistics Fee: ₹{logistics_fee}")
st.write(f"Platform Fee: ₹{commission}")
st.write(f"**Total Amount: ₹{total}**")
st.markdown("</div>", unsafe_allow_html=True)

# -------- Assign Farmer (Demo Logic) --------
def assign_farmer(region):
    for fid, f in st.session_state.farmers.items():
        if f["region"] == region and f["available"]:
            return fid
    return None

# -------- Place Order --------
if st.button("📦 Place Order"):
    farmer_id = assign_farmer(buyer["region"])

    if not farmer_id:
        st.error("No farmer available in your region")
    else:
        order_id = str(uuid.uuid4())[:8]

        st.session_state.orders[order_id] = {
            "buyer_id": buyer_id,
            "farmer_id": farmer_id,
            "product": product,
            "quantity": quantity,
            "price": base_price,
            "logistics": logistics_fee,
            "commission": commission,
            "total": total,
            "status": "Order Placed",
            "timestamps": {
                "created": datetime.now().strftime("%H:%M:%S")
            }
        }

        st.success("Order placed successfully!")

# -------- Order History --------
st.divider()
st.subheader("📜 Order History")

for oid, o in st.session_state.orders.items():
    if o["buyer_id"] == buyer_id:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write(f"**Order ID:** {oid}")
        st.write(f"Product: {o['product']}")
        st.write(f"Quantity: {o['quantity']}")
        st.write(f"Total: ₹{o['total']}")
        st.write(f"Status: {o['status']}")

        # -------- Reorder --------
        if st.button(f"🔁 Reorder {oid}"):
            new_id = str(uuid.uuid4())[:8]
            new_order = o.copy()
            new_order["timestamps"] = {
                "created": datetime.now().strftime("%H:%M:%S")
            }
            new_order["status"] = "Order Placed"
            st.session_state.orders[new_id] = new_order
            st.success("Order repeated")

        st.markdown("</div>", unsafe_allow_html=True)
