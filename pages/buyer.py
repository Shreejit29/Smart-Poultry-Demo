import streamlit as st
from datetime import datetime

st.title("🛒 Buyer Dashboard")

buyer = st.text_input("Buyer Name", "Demo Buyer")
region = st.selectbox("Region", ["Pune", "Mumbai", "Nashik", "Nagpur"])
product = st.selectbox("Product", ["Broiler Chicken", "Eggs", "Country Chicken"])
qty = st.number_input("Quantity", min_value=1, value=10)

price_map = {"Broiler Chicken": 120, "Eggs": 6, "Country Chicken": 180}
total_price = qty * price_map[product]

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.write(f"💰 **Total Amount:** ₹{total_price}")

if st.button("➡️ Proceed to Payment"):
    st.session_state.pay = True

st.markdown("</div>", unsafe_allow_html=True)

# ---------- FAKE PAYMENT ----------
if st.session_state.get("pay", False):
    st.subheader("💳 Payment (Demo)")
    method = st.radio("Payment Method", ["UPI", "Card", "Cash on Delivery"])

    if st.button("✅ Pay Now"):
        commission = int(total_price * 0.05)

        st.session_state.orders.append({
            "buyer": buyer,
            "region": region,
            "product": product,
            "quantity": qty,
            "amount": total_price,
            "commission": commission,
            "payment": method,
            "status": "Paid",
            "farmer": "Demo Farmer",
            "time": datetime.now().strftime("%H:%M:%S")
        })

        st.session_state.pay = False
        st.success("Payment successful! Order placed 🎉")

# ---------- ORDER HISTORY ----------
st.subheader("📜 Your Orders")

for o in st.session_state.orders:
    st.markdown(f"""
    <div class='card'>
    <b>{o['product']}</b><br>
    Qty: {o['quantity']}<br>
    Amount: ₹{o['amount']}<br>
    Status: {o['status']}
    </div>
    """, unsafe_allow_html=True)
