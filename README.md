# IT Help Desk Analytics

An end-to-end data analytics project that analyzes IT support tickets to evaluate operational performance, SLA compliance, resolution efficiency, customer satisfaction, and escalation trends.

## Project Overview

IT support teams need to resolve tickets efficiently while maintaining service quality and meeting Service Level Agreements (SLAs). This project analyzes **5,000 IT help desk tickets** to identify performance gaps, understand ticket patterns, and generate actionable business insights using Python, SQL, MySQL, and Power BI.

## Objectives

- Analyze IT help desk ticket trends and operational performance.
- Measure SLA compliance and identify potential service bottlenecks.
- Evaluate resolution time, customer satisfaction, and escalation rates.
- Compare ticket volumes and performance across categories, priorities, and support tiers.
- Build an interactive Power BI dashboard for data-driven decision-making.

## Tools and Technologies

- **Python:** Data cleaning, preprocessing, and exploratory data analysis
- **Pandas and NumPy:** Data manipulation and analysis
- **Matplotlib and Seaborn:** Data visualization
- **MySQL:** Data storage and SQL-based analysis
- **SQL:** Aggregations, filtering, and business KPI calculations
- **Power BI:** Interactive dashboard, KPI cards, charts, and slicers
- **Git and GitHub:** Version control and project documentation

## Key Performance Indicators (KPIs)

| KPI | Result |
|---|---:|
| Total Tickets | 5,000 |
| Closed Tickets | 3,877 |
| Average Resolution Time | 12.30 hours |
| Average Customer Satisfaction | 4.48 / 5 |
| SLA Compliance | 61.52% |
| Reopen Rate | 4.30% |
| Escalation Rate | 8.02% |

*Note: KPI values reflect the analysis performed on the project dataset.*

## Key Business Insights

1. **High ticket volume:** Network-related issues were the largest ticket category, with approximately 897 tickets.
2. **Resolution bottleneck:** Security tickets had the longest average resolution time, at approximately 15.37 hours.
3. **SLA performance gap:** Critical-priority tickets had an SLA compliance rate of approximately 48.62%.
4. **Customer satisfaction:** Satisfaction scores generally declined as resolution time increased.
5. **Support tier analysis:** Comparing L1, L2, and L3 performance helps identify differences in ticket handling and resolution efficiency.

## Power BI Dashboard

The Power BI dashboard provides an interactive view of help desk performance, including:

- KPI cards for ticket volume, resolution time, satisfaction, and SLA compliance
- Ticket analysis by category and priority
- Resolution-time and customer-satisfaction analysis
- SLA performance and escalation trends
- Interactive slicers for exploring ticket segments

### Dashboard Preview

*Dashboard screenshots will be added here.*

<!-- After creating the screenshots folder and saving the image, uncomment the next line:
![IT Help Desk Analytics Dashboard](assets/dashboard_overview.png)
-->

## Project Structure

```text
IT_help_desk/
├── data/
├── power bi/
│   └── dashboard.pbix
├── sql/
│   └── helpdesk_analysis.sql
├── src/
│   ├── cleaned.py
│   ├── dataset.py
│   └── eda_analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How to Run the Python Analysis

### 1. Clone the repository

```bash
git clone https://github.com/harshitagupta10130-ops/IT-Help-Desk-Analytics.git
cd IT-Help-Desk-Analytics
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

Review the Python scripts in the `src/` folder and run the relevant script according to its entry point and data-file requirements.

### 5. Explore the Power BI dashboard

Open `power bi/dashboard.pbix` in Microsoft Power BI Desktop.

**Note:** The dataset is not necessarily included in the repository. You may need to supply the source data and update file paths before rerunning the analysis.

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- SQL querying and KPI calculations
- Data visualization and dashboard development
- Business performance analysis
- Data storytelling and insight generation
- Version control using Git and GitHub

## Future Improvements

- Add dashboard screenshots and a project demonstration.
- Automate data refresh and KPI reporting.
- Introduce deeper SLA breach and ticket-resolution analysis.
- Develop predictive analytics for ticket resolution time.



