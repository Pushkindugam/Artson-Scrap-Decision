import streamlit as st
import matplotlib.pyplot as plt

# ---------------- Page Setup ---------------- #
st.set_page_config(page_title="Scrap Decision Tool – Artson", layout="centered")
st.markdown("<h1 style='text-align: center;'>Artson Ltd, A Tata Enterprise</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>♻️ Scrap Reuse vs Sell Decision</h2>", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/Pushkindugam/Artson-Scrap-Decision/main/artson_logo.png",
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

# ---------------- Material Info ---------------- #
material_type = st.selectbox("Scrap Material Type", [
    "Mild Steel (MS)", "Stainless Steel (SS)", "Carbon Steel",
    "Aluminum", "Copper", "Brass", "Cast Iron", "Custom Material"
])

density = st.number_input(f"Enter density for {material_type} (kg/m³)", min_value=100.0, max_value=20000.0, value=7850.0)

# ---------------- Input Section ---------------- #
st.header("📥 Input Parameters")

total_required_output = st.number_input("Total material required (kg)", value=1000)

input_type = st.radio("Input scrap as:", ["Weight (kg)", "Volume (m³)"])
if input_type == "Weight (kg)":
    scrap_available = st.number_input("Scrap available (kg)", value=1000.0)
else:
    volume = st.number_input("Scrap volume (m³)", value=0.5)
    scrap_available = volume * density
    st.info(f"Estimated scrap weight: **{scrap_available:.1f} kg** (based on density {density} kg/m³)")

scrap_quality = st.slider("Scrap quality factor (0–1)", 0.0, 1.0, 0.6)

# ---------------- Scrap Value Assessment ---------------- #
st.markdown("### 📊 Scrap Value Assessment")
market_price = st.number_input("Market price of scrap (₹ per kg)", value=24.0)

if market_price < 30:
    value_level = "🔴 Low Value"
elif market_price < 100:
    value_level = "🟡 Medium Value"
else:
    value_level = "🟢 High Value"

st.write(f"- **Entered Market Price:** ₹{market_price}/kg")
st.write(f"- **Scrap Classification:** {value_level}")

# Insight based on quality and material
if material_type in ["Stainless Steel (SS)", "Copper", "Brass"] and scrap_quality > 0.5:
    st.success(f"🧠 Insight: {material_type} is high value and reusable – prefer reuse.")
elif market_price < 30 and scrap_quality < 0.4:
    st.warning("🧠 Insight: Low quality & low value – consider selling.")

# ---------------- Cost Inputs ---------------- #
with st.expander("🚚 Reuse Cost Parameters"):
    transport_cost_per_kg = st.number_input("Transport cost (₹ per kg)", value=3.0)
    processing_cost_per_kg = st.number_input("Processing cost (₹ per kg)", value=4.5)

with st.expander("💸 Market Rates"):
    new_material_cost = st.number_input("New material cost (₹ per kg)", value=56.0)
    scrap_sale_price = st.number_input("Scrap sale price at site (₹ per kg)", value=market_price)

# ---------------- Main Logic ---------------- #
if st.button("🔍 Compare Options"):
    reusable_weight = scrap_available * scrap_quality
    shortfall = max(0, total_required_output - reusable_weight)

    transport_cost = scrap_available * transport_cost_per_kg
    processing_cost = scrap_available * processing_cost_per_kg
    fresh_topup_cost = shortfall * new_material_cost

    total_cost_reuse = transport_cost + processing_cost + fresh_topup_cost
    total_cost_sell_buy = total_required_output * new_material_cost - scrap_available * scrap_sale_price

    # ---------------- Recommendation ---------------- #
    st.subheader("🧭 Recommended Strategy")
    if total_cost_reuse < total_cost_sell_buy:
        st.success("✅ **REUSE SCRAP + BUY TOP-UP** is more economical.")
    else:
        st.warning("✅ **SELL SCRAP & BUY NEW MATERIAL** is more economical.")

    # ---------------- Cost Comparison ---------------- #
    st.subheader("💰 Cost Comparison")
    st.write(f"**Reuse + Top-up Cost:** ₹{total_cost_reuse:,.2f}")
    st.write(f"**Sell & Buy New Cost:** ₹{total_cost_sell_buy:,.2f}")

    # ---------------- Plot ---------------- #
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

    # ---------------- Suggestions ---------------- #
    with st.expander("💡 Feature Suggestions"):
        st.markdown("""
        - 📤 Export this report as PDF/Excel  
        - 📊 Sensitivity analysis on quality & market price  
        - ♻️ Estimate carbon savings from reuse  
        - 🔗 Link to inventory management or ERP system  
        """)



















# import os
# import streamlit as st
# import matplotlib.pyplot as plt

# # ---------------- Page Setup ---------------- #
# st.set_page_config(page_title="Scrap Decision Tool – Artson", layout="centered")
# st.markdown("<h1 style='text-align: center;'>Artson Ltd, A Tata Enterprise</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center;'>♻️ Scrap Reuse vs Sell Decision</h2>", unsafe_allow_html=True)

# # ---------------- Sidebar ---------------- #
# with st.sidebar:
#     st.image(
#         "https://raw.githubusercontent.com/Pushkindugam/Artson-Steel-WPI-Prediction-Seasonality/main/artson_logo.png",
#         use_container_width=True,
#         caption="Artson Engineering Ltd."
#     )

#     st.markdown("## ♻️ Why Scrap Matters?")
#     st.markdown("""
#     Scrap is **not waste**—it holds **economic and environmental value**.  
#     Efficient reuse can save costs, reduce procurement pressure,  
#     and support **sustainable EPC operations**.
#     """)

#     st.markdown("---")
#     st.markdown("### 🛠️ Built by Artson SCM Team – 2025")
#     st.markdown("*by **Pushkin Dugam***")
#     st.markdown("[🔗 GitHub Repository](https://github.com/Pushkindugam/Artson-Steel-WPI-Prediction-Seasonality)")

# # ---------------- Input Section ---------------- #
# st.header("📥 Input Parameters")

# total_required_output = st.number_input("Total material required (kg)", value=1000)

# with st.expander("🔧 Scrap Details"):
#     scrap_available = st.number_input("Scrap available (kg)", value=1000)
#     scrap_quality = st.slider("Scrap quality factor (0–1)", 0.0, 1.0, 0.6)

# with st.expander("🚚 Reuse Cost Parameters"):
#     transport_cost_per_kg = st.number_input("Transport cost (₹ per kg)", value=3.0)
#     processing_cost_per_kg = st.number_input("Processing cost (₹ per kg)", value=4.5)

# with st.expander("💸 Market Rates"):
#     new_material_cost = st.number_input("New material cost (₹ per kg)", value=56.0)
#     scrap_sale_price = st.number_input("Scrap sale price at site (₹ per kg)", value=24.0)

# # ---------------- Main Logic ---------------- #
# if st.button("🔍 Compare Options"):
#     # ⚙️ Calculations
#     reusable_weight = scrap_available * scrap_quality
#     shortfall = max(0, total_required_output - reusable_weight)

#     transport_cost = scrap_available * transport_cost_per_kg
#     processing_cost = scrap_available * processing_cost_per_kg
#     fresh_topup_cost = shortfall * new_material_cost

#     total_cost_reuse = transport_cost + processing_cost + fresh_topup_cost
#     total_cost_sell_buy = total_required_output * new_material_cost - scrap_available * scrap_sale_price

#     # ---------------- Recommendation ---------------- #
#     st.subheader("🧭 Recommended Strategy")
#     if total_cost_reuse < total_cost_sell_buy:
#         st.success("✅ **REUSE SCRAP + BUY TOP-UP** is more economical.")
#     else:
#         st.warning("✅ **SELL SCRAP & BUY NEW MATERIAL** is more economical.")

#     # ---------------- Cost Comparison ---------------- #
#     st.subheader("💰 Cost Comparison")
#     st.write(f"**Reuse + Top-up Cost:** ₹{total_cost_reuse:,.2f}")
#     st.write(f"**Sell & Buy New Cost:** ₹{total_cost_sell_buy:,.2f}")

#     # ---------------- Plot ---------------- #
#     labels = ["Reuse + Top-up", "Sell & Buy New"]
#     costs = [total_cost_reuse, total_cost_sell_buy]
#     colors = ["#00b300", "#ff6600"]

#     fig, ax = plt.subplots()
#     bars = ax.bar(labels, costs, color=colors)
#     ax.set_ylabel("Total Cost (₹)")
#     ax.set_title("Cost Comparison")

#     for bar in bars:
#         height = bar.get_height()
#         ax.annotate(f'₹{height:,.0f}',
#                     xy=(bar.get_x() + bar.get_width() / 2, height),
#                     xytext=(0, 6),
#                     textcoords="offset points",
#                     ha='center', va='bottom')

#     st.pyplot(fig)















# import os
# import streamlit as st
# import matplotlib.pyplot as plt

# # Avoid permission error
# os.environ["STREAMLIT_CONFIG_DIR"] = os.path.expanduser("~/.streamlit")
# os.makedirs(os.environ["STREAMLIT_CONFIG_DIR"], exist_ok=True)

# # ---------------- Sidebar ---------------- #
# with st.sidebar:
#     st.image(
#         "https://raw.githubusercontent.com/Pushkindugam/Artson-Steel-WPI-Prediction-Seasonality/main/artson_logo.png",
#         use_container_width=True,
#         caption="Artson Engineering Ltd."
#     )

#     st.markdown("## ♻️ Why Scrap Matters?")
#     st.markdown("""
#     Scrap is **not waste**—it holds **economic and environmental value**.  
#     Efficient reuse can save costs, reduce procurement pressure,  
#     and support **sustainable EPC operations**.
#     """)

#     st.markdown("---")
#     st.markdown("### 🛠️ Built by Artson SCM Team – 2025")
#     st.markdown("*by **Pushkin Dugam***")
#     st.markdown("[🔗 GitHub Repository](https://github.com/Pushkindugam/Artson-Steel-WPI-Prediction-Seasonality)")

# # ---------------- Main App ---------------- #
# st.title("♻️ Scrap Reuse vs Sell Decision – Artson EPC")

# st.markdown("""
# This tool compares two strategies for scrap handling:
# - **Reuse scrap** (and top-up fresh material if needed)
# - **Sell scrap at site and buy fresh material**

# It recommends the cheaper option based on real EPC parameters.
# """)

# # 📥 Input Fields
# st.header("📥 Input Parameters")

# total_required_output = st.number_input("Total material required (kg)", value=1000)

# with st.expander("🔧 Scrap Details"):
#     scrap_available = st.number_input("Scrap available (kg)", value=1000)
#     scrap_quality = st.slider("Scrap quality factor (0–1)", 0.0, 1.0, 0.6)

# with st.expander("🚚 Reuse Cost Parameters"):
#     transport_cost_per_kg = st.number_input("Transport cost (₹ per kg)", value=3.0)
#     processing_cost_per_kg = st.number_input("Processing cost (₹ per kg)", value=4.5)

# with st.expander("💸 Market Rates"):
#     new_material_cost = st.number_input("New material cost (₹ per kg)", value=56.0)
#     scrap_sale_price = st.number_input("Scrap sale price at site (₹ per kg)", value=24.0)

# # 🔍 Compute on click
# if st.button("🔍 Compare Options"):
#     # ⚙️ Calculations
#     reusable_weight = scrap_available * scrap_quality
#     shortfall = max(0, total_required_output - reusable_weight)

#     transport_cost = scrap_available * transport_cost_per_kg
#     processing_cost = scrap_available * processing_cost_per_kg
#     fresh_topup_cost = shortfall * new_material_cost

#     total_cost_reuse = transport_cost + processing_cost + fresh_topup_cost
#     total_cost_sell_buy = total_required_output * new_material_cost - scrap_available * scrap_sale_price

#     # 💰 Results
#     st.subheader("💰 Cost Comparison")
#     st.write(f"**Reuse + Top-up Cost:** ₹{total_cost_reuse:,.2f}")
#     st.write(f"**Sell & Buy New Cost:** ₹{total_cost_sell_buy:,.2f}")

#     # 📊 Bar Chart
#     labels = ["Reuse + Top-up", "Sell & Buy New"]
#     costs = [total_cost_reuse, total_cost_sell_buy]
#     colors = ["#00b300", "#ff6600"]

#     fig, ax = plt.subplots()
#     bars = ax.bar(labels, costs, color=colors)
#     ax.set_ylabel("Total Cost (₹)")
#     ax.set_title("Cost Comparison")

#     for bar in bars:
#         height = bar.get_height()
#         ax.annotate(f'₹{height:,.0f}',
#                     xy=(bar.get_x() + bar.get_width() / 2, height),
#                     xytext=(0, 6),
#                     textcoords="offset points",
#                     ha='center', va='bottom')

#     st.pyplot(fig)

#     # ✅ Recommendation
#     if total_cost_reuse < total_cost_sell_buy:
#         st.success("✅ Recommended: REUSE SCRAP + BUY TOP-UP")
#     else:
#         st.warning("✅ Recommended: SELL SCRAP & BUY NEW")








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
