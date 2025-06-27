import os
import streamlit as st
import matplotlib.pyplot as plt

# Avoid permission error
os.environ["STREAMLIT_CONFIG_DIR"] = os.path.expanduser("~/.streamlit")
os.makedirs(os.environ["STREAMLIT_CONFIG_DIR"], exist_ok=True)

# ---------------- Sidebar ---------------- #
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/Pushkindugam/Artson-Steel-WPI-Prediction-Seasonality/main/artson_logo.png",
        use_container_width=True,
        caption="Artson Engineering Ltd."
    )

    st.markdown("## ♻️ Why Scrap Matters?")
    st.markdown("""
    Scrap is **not waste**—it holds **economic and environmental value**.  
    Efficient reuse can save costs, reduce procurement pressure,  
    and support **sustainable EPC operations**.
    """)

    st.markdown("---")
    st.markdown("### 🛠️ Built by Artson SCM Team – 2025")
    st.markdown("*by **Pushkin Dugam***")
    st.markdown("[🔗 GitHub Repository](https://github.com/Pushkindugam/Artson-Steel-WPI-Prediction-Seasonality)")

# ---------------- Main App ---------------- #
st.title("♻️ Scrap Reuse vs Sell Decision – Artson EPC")

st.markdown("""
This tool compares two strategies for scrap handling:
- **Reuse scrap** (and top-up fresh material if needed)
- **Sell scrap at site and buy fresh material**

It recommends the cheaper option based on real EPC parameters.
""")

# 📥 Input Fields
st.header("📥 Input Parameters")

total_required_output = st.number_input("Total material required (kg)", value=1000)

with st.expander("🔧 Scrap Details"):
    scrap_available = st.number_input("Scrap available (kg)", value=1000)
    scrap_quality = st.slider("Scrap quality factor (0–1)", 0.0, 1.0, 0.6)

with st.expander("🚚 Reuse Cost Parameters"):
    transport_cost_per_kg = st.number_input("Transport cost (₹ per kg)", value=3.0)
    processing_cost_per_kg = st.number_input("Processing cost (₹ per kg)", value=4.5)

with st.expander("💸 Market Rates"):
    new_material_cost = st.number_input("New material cost (₹ per kg)", value=56.0)
    scrap_sale_price = st.number_input("Scrap sale price at site (₹ per kg)", value=24.0)

# 🔍 Compute on click
if st.button("🔍 Compare Options"):
    # ⚙️ Calculations
    reusable_weight = scrap_available * scrap_quality
    shortfall = max(0, total_required_output - reusable_weight)

    transport_cost = scrap_available * transport_cost_per_kg
    processing_cost = scrap_available * processing_cost_per_kg
    fresh_topup_cost = shortfall * new_material_cost

    total_cost_reuse = transport_cost + processing_cost + fresh_topup_cost
    total_cost_sell_buy = total_required_output * new_material_cost - scrap_available * scrap_sale_price

    # 💰 Results
    st.subheader("💰 Cost Comparison")
    st.write(f"**Reuse + Top-up Cost:** ₹{total_cost_reuse:,.2f}")
    st.write(f"**Sell & Buy New Cost:** ₹{total_cost_sell_buy:,.2f}")

    # 📊 Bar Chart
    labels = ["Reuse + Top-up", "Sell & Buy New"]
    costs = [total_cost_reuse, total_cost_sell_buy]
    colors = ["#00b300", "#ff6600"]

    fig, ax = plt.subplots()
    bars = ax.bar(labels, costs, color=colors)
    ax.set_ylabel("Total Cost (₹)")
    ax.set_title("Cost Comparison")

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'₹{height:,.0f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 6),
                    textcoords="offset points",
                    ha='center', va='bottom')

    st.pyplot(fig)

    # ✅ Recommendation
    if total_cost_reuse < total_cost_sell_buy:
        st.success("✅ Recommended: REUSE SCRAP + BUY TOP-UP")
    else:
        st.warning("✅ Recommended: SELL SCRAP & BUY NEW")








# import os

# # Avoid permission error in Hugging Face by setting config dir
# os.environ["STREAMLIT_CONFIG_DIR"] = os.path.expanduser("~/.streamlit")
# os.makedirs(os.environ["STREAMLIT_CONFIG_DIR"], exist_ok=True)


# import streamlit as st

# st.title("♻️ Scrap Reuse vs Sell Decision – Artson EPC")

# st.markdown("""
# This tool compares two strategies for scrap handling:
# - **Reuse scrap** (and top-up fresh material if needed)
# - **Sell scrap at site and buy fresh material**

# It recommends the cheaper option based on real EPC parameters.
# """)

# # 🚀 Input fields
# st.header("📥 Input Parameters")

# total_required_output = st.number_input("Total material required (kg)", value=100000)
# scrap_available = st.number_input("Scrap available (kg)", value=100000)
# transport_cost_per_kg = st.number_input("Flat transport cost (₹ per kg)", value=3.0)
# processing_cost_per_kg = st.number_input("Processing cost (₹ per kg)", value=4.5)
# scrap_quality = st.slider("Scrap quality factor (0–1)", 0.0, 1.0, 0.6)
# new_material_cost = st.number_input("New material cost (₹ per kg)", value=56.0)
# scrap_sale_price = st.number_input("Scrap sale price at site (₹ per kg)", value=24.0)

# if st.button("🔍 Compare Options"):
#     # ⚙️ Computations
#     reusable_weight = scrap_available * scrap_quality
#     shortfall = max(0, total_required_output - reusable_weight)

#     transport_cost = scrap_available * transport_cost_per_kg
#     processing_cost = scrap_available * processing_cost_per_kg
#     fresh_topup_cost = shortfall * new_material_cost

#     total_cost_reuse = transport_cost + processing_cost + fresh_topup_cost
#     total_cost_sell_buy = total_required_output * new_material_cost - scrap_available * scrap_sale_price

#     # 📊 Display results
#     st.subheader("💰 Cost Comparison")
#     st.write(f"**Reuse + Top-up Cost:** ₹{total_cost_reuse:,.2f}")
#     st.write(f"**Sell & Buy New Cost:** ₹{total_cost_sell_buy:,.2f}")

#     # ✅ Recommendation
#     if total_cost_reuse < total_cost_sell_buy:
#         st.success("✅ Recommended: REUSE SCRAP + BUY TOP-UP")
#     else:
#         st.warning("✅ Recommended: SELL SCRAP & BUY NEW")
