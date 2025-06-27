# ♻️ Artson Scrap Reuse vs Sell Decision Tool

An intelligent logistics and procurement decision support tool built for **Artson Engineering Ltd. (A Tata Enterprise)**.

This Streamlit web app helps you evaluate whether to:

- 🚚 **Transport and reuse scrap** at the manufacturing site  
- 💰 **Sell scrap at the project site and buy fresh material**

It incorporates real-world EPC factors like transport, processing cost, material quality degradation, and resale value to recommend the **most cost-effective** strategy.

🔗 **Live App:**  
👉 [https://artson-scrap-decision-4mkabtay94pusqbbwc8eft.streamlit.app/](https://artson-scrap-decision-4mkabtay94pusqbbwc8eft.streamlit.app/)

---

## 📦 What It Does

- Calculates **total reuse cost** (transport + processing + top-up material)
- Calculates **cost of selling scrap and buying fresh material**
- Adjusts calculations for **scrap quality degradation**
- Recommends the more economical path using a logic-based comparison

---

## 📸 Screenshots

| Input Screen | Output Screen |
|--------------|---------------|
| ![Input](https://github.com/Pushkindugam/Artson-Scrap-Decision/blob/main/Scrap_input_screenshot.png?raw=true) | ![Output](https://github.com/Pushkindugam/Artson-Scrap-Decision/blob/main/Scrap_output_screenshot.png?raw=true) |

---

## 🧠 Key Features

| Feature                           | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| 📊 Quality-based recovery         | Accounts for % loss during reuse (e.g., 60% quality = 40% scrap loss)       |
| 💰 Total reuse cost calc          | Transport + Processing + Top-up new material                                |
| 🔁 Smart cost comparison          | Compares Reuse vs Sell+Buy options to minimize cost                         |
| 🧠 Strategy Insights              | Contextual material guidance based on price & scrap quality                 |
| 🌐 Web-based access               | Streamlit app accessible without login from any browser                     |

---

## 🛠️ How to Use

1. **Enter parameters** such as:
   - Total material requirement
   - Scrap availability (weight or volume)
   - Material type and quality
   - Transport, processing, and resale costs
2. **Click “Compare Options”**
3. View:
   - Classification of material (low/medium/high value)
   - Cost comparison
   - Final recommendation (reuse or sell)

---

## 🏗️ Built For

> **Artson Engineering Ltd. (A Tata Enterprise)**  
> *By Pushkin Dugam (B.Tech Mechanical, IIT Jodhpur)*

Supports smart decision-making in:

- Procurement Strategy  
- Site Logistics Planning  
- Cost Optimization in EPC Projects  
- Sustainable Material Utilization

---

## 📤 Local Run Instructions

Clone the repository and run the app locally:

```bash
git clone https://github.com/Pushkindugam/Artson-Scrap-Decision.git
cd Artson-Scrap-Decision
pip install -r requirements.txt
streamlit run streamlit_app.py
