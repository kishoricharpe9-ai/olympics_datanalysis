# 🏅 Olympic History Data Analysis Web App

An interactive Exploratory Data Analysis (EDA) dashboard built with **Python**, **Streamlit**, and **Plotly**. This application dives into 120 years of modern Olympic Games history (1896–2016), enabling users to explore medal tallies, historical participation trends, country-level performance, and athlete demographics.

---

## ✨ Key Features

* **🥇 Medal Tally:** Filter dynamic medal tables by **Year** and **Country** (or view the all-time overall standings).
* **📊 Overall Analysis:** View key high-level statistics (total editions, host cities, sports, events, participating nations, and athletes) alongside interactive trend lines over time.
* **🌍 Country-Wise Analysis:** Deep dive into any specific nation's Olympic journey, medal progression across years, sport-wise heatmap, and top-performing athletes.
* **🏃 Athlete-Wise Analysis:** Explore interactive age distributions for medalists across various sports, height-vs-weight scatter plots by gender and medal type, and male-vs-female participation trends over the years.

---

## 🛠️ Tech Stack

* **Frontend & Web Framework:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Interactive Visualizations:** [Plotly](https://plotly.com/python/),[Seaborn]

---

## 📂 Project Structure

```text
├── app.py                  # Main Streamlit application & UI routing
├── preprocessor.py         # Data cleaning and Summer Olympics filtering
├── helper.py               # Analytical functions for tallies, trends, and distributions
├── athlete_events.csv      # Dataset containing athlete-level Olympic records
├── noc_regions.csv         # Dataset mapping NOC codes to country/region names
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
🚀 Getting Started
1. Clone the repository
Bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
2. Install dependencies
Make sure you have Python installed, then install the required packages:

Bash
pip install streamlit pandas numpy plotly
3. Run the Streamlit app
Bash
streamlit run app.py
The app will automatically open in your default browser at http://localhost:8501.

📊 Dataset
This project uses the 120 Years of Olympic History: Athletes and Results dataset (athlete_events.csv and noc_regions.csv), covering every Olympic Games from Athens 1896 to Rio 2016.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.
