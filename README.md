# ♻️ Artson Scrap Reuse vs Sell Decision Tool

An intelligent logistics and procurement decision support tool built for **Artson Engineering Ltd.**

This Streamlit app helps you decide whether to:
- 🚚 **Transport and reuse scrap** at the manufacturing site
- 💰 **Sell scrap at the project site and buy fresh material**

It uses real-world EPC cost factors like transport, processing, quality degradation, and scrap resale value to recommend the most cost-effective option.

🔗 **Live App:**  
👉 [https://artson-scrap-decision-4mkabtay94pusqbbwc8eft.streamlit.app/](https://artson-scrap-decision-4mkabtay94pusqbbwc8eft.streamlit.app/)

---

## 📦 What It Does

- Calculates the **cost of reusing scrap**, including transport and processing
- Calculates the **net cost of selling scrap on-site and buying fresh**
- Factors in **scrap quality degradation**
- Provides a clear, **data-backed recommendation**

---

## 📸 Screenshot

<img src="https://github.com/Pushkindugam/Artson-Scrap-Decision/blob/main/Scrap-Decision.png" alt="Artson Scrap Decision Screenshot" width="720"/>

---

## 🧠 Key Features

| Feature                           | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| 📊 Quality-based recovery          | Accounts for % loss during reuse (e.g., 60% quality = 40% scrap loss)       |
| 💰 Total reuse cost calc           | Transport + Processing + Top-up new material                                |
| 🔁 Smart comparison                | Sell scrap vs. reuse + top-up logic                                         |
| 🌐 Web-based access                | Built with Streamlit and accessible without login                           |

---

## 🛠️ How to Use

1. Enter inputs like:
   - Scrap quantity and quality
   - Transport cost per kg
   - Distance
   - Processing cost, new material cost, and resale value
2. Click **“Compare Options”**
3. The tool shows both strategies and recommends the lower-cost one

---

## 🏗️ Built For

> Artson Engineering Ltd. (A Tata Enterprise)  
> By Pushkin Dugam (B.Tech Mechanical, IIT Jodhpur)

Supports decision-making in:
- Procurement Strategy
- Site Logistics Planning
- Cost Optimization in EPC Projects

---

## 📤 Local Run

```bash
pip install streamlit
streamlit run streamlit_app.py
