# ⚡ Electricity Consumption Analysis in India

### Plugging into the Future — An Exploration of Electricity Consumption Patterns

---

## 📌 Project Overview

Electricity demand is a critical indicator of economic growth, population needs, and regional development. This project analyzes electricity consumption patterns across Indian states and regions to uncover trends, disparities, and insights that can support better planning and decision-making.

Using a combination of database management, SQL processing, Tableau visualization, and web integration with Flask, we built an end-to-end analytics solution that transforms raw data into meaningful insights through interactive dashboards and storytelling.

---

## 🎯 Objectives

* Analyze electricity usage across states and regions of India
* Identify high and low consumption areas
* Compare consumption trends over time (2019 vs 2020)
* Enable interactive exploration through filters
* Present insights via dashboards and storyboards
* Integrate visualizations into a web interface

---

## 🧰 Tools & Technologies Used

* **Python** — Basic scripting and integration
* **SQLite (DB Browser)** — Data storage
* **SQL** — Data cleaning and querying
* **Tableau Public** — Data visualization & dashboards
* **Flask** — Web integration
* **HTML/CSS** — UI embedding

---

## 📂 Dataset

The dataset contains electricity consumption records for multiple Indian states with the following attributes:

* State
* Region
* Latitude
* Longitude
* Date
* Electricity Usage

The data was pre-cleaned but further reviewed for accuracy and usability before analysis.

---

## 🗄️ Step 1 — Data Acquisition & Validation

We obtained the finalized dataset in CSV format and verified:

* Data completeness
* Correct formatting
* Consistent date values
* Valid numerical usage values
* Absence of major missing data

This ensured the dataset was ready for database storage and visualization.

---

## 🗄️ Step 2 — Data Storage & SQL Processing

The dataset was imported into a structured SQLite database.

SQL operations performed included:

* Viewing and verifying records
* Filtering by region and usage
* Removing null values
* Sorting and aggregating consumption
* Creating a cleaned dataset table

These steps ensured efficient querying and reliable downstream analysis.

---

## 🔗 Step 3 — Connecting Database to Tableau

The processed data was exported from the database and connected to Tableau Public. This enabled visualization without directly modifying the original data.

---

## 🧹 Step 4 — Data Preparation for Visualization

Even though the dataset was clean, we performed additional preparation:

* Verified data types (dates, numbers, text)
* Assigned geographic roles for mapping
* Renamed fields for clarity
* Explored value distributions
* Created optional calculated fields
* Applied relevant filters

This step ensured accurate and meaningful visual outputs.

---

## 📊 Step 5 — Unique Visualizations Created

We developed multiple visualizations to analyze consumption patterns:

### 📈 Yearly Consumption (2019 vs 2020)

Comparison of electricity usage between two years to identify growth or decline.

### 🔢 Total Consumption

A KPI view showing overall electricity usage across the dataset.

### 🌍 Usage by Region

Bar chart comparing consumption across regions of India.

### 🏆 Top Consuming States

Identification of states with the highest electricity demand.

### 📉 Lowest Consuming States

Identification of states with minimal electricity usage.

These visuals collectively provide a comprehensive analytical view.

---

## 🧭 Step 6 — Dashboard Design & Responsiveness

All visualizations were combined into a cohesive interactive dashboard designed with:

* Clear layout hierarchy
* User-centered design principles
* Responsive sizing
* Meaningful titles and labels
* Interactive filters
* Consistent color schemes

The dashboard enables quick understanding while allowing deeper exploration.

---

## 📖 Step 7 — Storyboard (Data Story)

A Tableau Story was created to guide users through insights step-by-step:

1. Overview of electricity consumption
2. Yearly trend comparison
3. Regional analysis
4. Top consuming states
5. Lowest consuming states
6. Final insights and conclusions

This storytelling approach makes complex data easier to interpret.

---

## 🗃️ Step 8 — Data Volume Monitoring

We analyzed the dataset size within the database:

* Number of rows (records)
* Number of columns (attributes)
* Query efficiency

This ensured the system handled data without performance issues.

---

## 🎛️ Step 9 — Utilization of Data Filters

Interactive filters were implemented on key dimensions:

* State
* Region
* Date / Year
* Top N / Bottom N

Filters improve performance and allow users to focus on specific segments of data, enhancing insight discovery.

---

## 🌐 Step 10 — Publishing to Tableau Public

The final dashboard and story were published online via Tableau Public, enabling:

* Easy sharing
* Public accessibility
* Interactive viewing
* Portfolio presentation

---

## 💻 Step 11 — Web Integration Using Flask

To demonstrate real-world deployment, the Tableau Story was embedded into a Flask web application using Tableau’s official embed code.

This allowed:

* Custom UI around the visualization
* Seamless integration into a website
* Future scalability for additional features

---

## 📊 Key Insights

* Significant variation in electricity usage across regions
* Certain states consistently dominate consumption
* Noticeable differences between 2019 and 2020 usage patterns
* Regional disparities highlight infrastructure and population factors

---

## 👥 Team Members

### 🧑‍💼 Team Lead

**Shivam Sharma**
📧 [shivam.2327csit1221@kiet.edu](mailto:shivam.2327csit1221@kiet.edu)

---

### 👨‍💻 Member

**Shivang Patel**
📧 [shivang.2327csit1139@kiet.edu](mailto:shivang.2327csit1139@kiet.edu)

---

### 👨‍💻 Member

**Shivansh Chhabra**
📧 [shivansh.2327csit104@kiet.edu](mailto:shivansh.2327csit104@kiet.edu)

---

### 👨‍💻 Member

**Shresth**
📧 [shresth.2327ec1024@kiet.edu](mailto:shresth.2327ec1024@kiet.edu)

---

## 🚀 Conclusion

This project demonstrates how raw data can be transformed into actionable insights through a structured analytics pipeline. By combining database management, visualization tools, and web technologies, we developed a comprehensive system for analyzing electricity consumption patterns in India.

The approach used in this project can be extended to energy planning, policy formulation, and infrastructure development.

---

## 📌 Future Enhancements

* Real-time data integration
* Predictive consumption modeling
* Advanced geographic analysis
* Mobile-friendly dashboard design
* Secure authentication for enterprise use

---

## 🙏 Acknowledgment

We thank our institution and mentors for their guidance and support throughout this project.

---

⭐ *If you found this project insightful, feel free to explore the dashboard and share your feedback.*
