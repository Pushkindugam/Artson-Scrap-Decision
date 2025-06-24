import streamlit as st

st.title("♻️ Scrap Reuse vs Sell Decision – Artson EPC")

st.markdown("""
This tool compares two strategies for scrap handling:
- **Reuse scrap** (and top-up fresh material if needed)
- **Sell scrap at site and buy fresh material**

It recommends the cheaper option based on real EPC parameters.
""")

# 🚀 Input fields
st.header("📥 Input Parameters")

total_required_output = st.number_input("Total material required (kg)", value=100000)
scrap_available = st.number_input("Scrap available (kg)", value=100000)
transport_cost_per_kg = st.number_input("Flat transport cost (₹ per kg)", value=3.0)
processing_cost_per_kg = st.number_input("Processing cost (₹ per kg)", value=4.5)
scrap_quality = st.slider("Scrap quality factor (0–1)", 0.0, 1.0, 0.6)
new_material_cost = st.number_input("New material cost (₹ per kg)", value=56.0)
scrap_sale_price = st.number_input("Scrap sale price at site (₹ per kg)", value=24.0)

if st.button("🔍 Compare Options"):
    # ⚙️ Computations
    reusable_weight = scrap_available * scrap_quality
    shortfall = max(0, total_required_output - reusable_weight)

    transport_cost = scrap_available * transport_cost_per_kg
    processing_cost = scrap_available * processing_cost_per_kg
    fresh_topup_cost = shortfall * new_material_cost

    total_cost_reuse = transport_cost + processing_cost + fresh_topup_cost
    total_cost_sell_buy = total_required_output * new_material_cost - scrap_available * scrap_sale_price

    # 📊 Display results
    st.subheader("💰 Cost Comparison")
    st.write(f"**Reuse + Top-up Cost:** ₹{total_cost_reuse:,.2f}")
    st.write(f"**Sell & Buy New Cost:** ₹{total_cost_sell_buy:,.2f}")

    # ✅ Recommendation
    if total_cost_reuse < total_cost_sell_buy:
        st.success("✅ Recommended: REUSE SCRAP + BUY TOP-UP")
    else:
        st.warning("✅ Recommended: SELL SCRAP & BUY NEW")
