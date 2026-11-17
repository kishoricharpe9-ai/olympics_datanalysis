# 🏅 120 Years of Olympic History: Data Analysis & Web Dashboard

An interactive Exploratory Data Analysis (EDA) dashboard built with **Python, Streamlit, and Plotly**. This application explores 120 years of modern Olympic Games history (1896–2016), enabling users to analyze medal tallies, historical participation trends, country-level performance, and athlete demographics.

🚀 **Live Interactive App**: [Live Streamlit DashBoard](https://olympicsdatanalysis-hduhxmsnw8mrdukvfrrwse.streamlit.app/)  
💻 **GitHub Repository**: [kishoricharpe9-ai/olympics_datanalysis](https://github.com/kishoricharpe9-ai/olympics_datanalysis)

---

## ✨ Key Features

* 🥇 **Medal Tally Analysis**: Filter dynamic medal tables by Year and Country (or view all-time standings).
* 📊 **Overall Statistics & Trends**: High-level metrics tracking the evolution of editions, host cities, sports, events, participating nations, and male-vs-female athlete ratios over time.
* 🌍 **Country-Wise Deep Dive**: Analyze a specific nation's Olympic journey, medal progression across editions, sport-wise heatmaps, and top-performing athletes.
* 🏃 **Athlete Demographics & Profiling**: Interactive age distributions of medalists, height-vs-weight scatter plots by sport/gender, and historical participation metrics.

---

## 🛠️ Tech Stack & Architecture

* **Language**: Python 3.10+
* **Web Framework**: Streamlit
* **Data Engineering & Manipulation**: Pandas, NumPy
* **Data Visualization**: Plotly, Seaborn, Matplotlib
* **Deployment**: Streamlit Community Cloud

---

## ⚙️ Data Pipeline & Technical Highlights

* **Data Cleaning & Integration**: Merged primary athlete records (`athlete_events.csv`) with National Olympic Committee region mapping (`noc_regions.csv`) to resolve historical country boundary changes.
* **Filtering & Scope**: Filtered analyses to Summer Olympic Games to ensure metric consistency across multi-decade trendlines.
* **Performance Optimization**: Implemented Streamlit caching (`@st.cache_data`) on data loading and preprocessing routines to enable sub-second filter updates.

---

## 📂 Project Structure

```text
├── code.py                      # Main Streamlit application & UI layout
├── preprocessor.py              # Data cleaning, NOC joining & Summer Olympics filter
├── helper.py                    # Analytical queries, aggregation logic & chart builders
├── athlete_events.zip           # Historical dataset of Olympic athlete records (1896-2016)
├── noc_regions.csv              # NOC region lookup table
├── olympic_games_analysis.ipynb # Initial Exploratory Data Analysis (EDA) notebook
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🚀 Local Setup & Installation

1. **Clone the repository**:

```bash
git clone https://github.com/kishoricharpe9-ai/olympics_datanalysis.git
cd olympics_datanalysis
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app locally**:

```bash
streamlit run code.py
```

The app will automatically open in your browser at `http://localhost:8501`.

---

## 📊 Dataset Attribution

This project utilizes the **120 Years of Olympic History: Athletes and Results** dataset, covering modern Olympic Games from Athens 1896 to Rio 2016.
