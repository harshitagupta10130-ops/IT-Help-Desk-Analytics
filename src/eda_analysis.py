from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

CLEANED_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "helpdesk_tickets_cleaned.csv"
)

df = pd.read_csv(CLEANED_FILE)

print("Dataset loaded successfully!")

print("\nDataset shape:")
print(df.shape)

print("\nTickets by Category:")
print(df["Category"].value_counts())

print("\nTickets by Priority:")
print(df["Priority"].value_counts())

print("\nTickets by Department:")
print(df["Department"].value_counts())

print("\nAverage Resolution Time:")

avg_resolution = df["Resolution_Time_Hours"].mean()

print(f"{avg_resolution:.2f} hours")

print("\nSLA Performance:")
print(df["SLA_Status"].value_counts())


closed_tickets = df[df["SLA_Status"].isin(["Met", "Breached"])]

sla_compliance = (
    (closed_tickets["SLA_Status"] == "Met").mean() * 100
)

print("\nSLA Compliance:")
print(f"{sla_compliance:.2f}%")

print("\nTickets by Month:")

monthly_tickets = (
    df.groupby("Month_Name")
    .size()
)

print(monthly_tickets)


df["Created_DateTime"] = pd.to_datetime(df["Created_DateTime"])

df["Year_Month"] = df["Created_DateTime"].dt.to_period("M")

monthly_trend = (
    df.groupby("Year_Month")
    .size()
)

print("\nMonthly Ticket Trend:")
print(monthly_trend)

print("\nTickets by Day of Week:")

day_tickets = (
    df["Day_Name"]
    .value_counts()
)

print(day_tickets)

print("\nTickets by Hour:")

hourly_tickets = (
    df["Created_Hour"]
    .value_counts()
    .sort_index()
)

print(hourly_tickets)

print("\nReopened Tickets:")
print(df["Reopened"].value_counts())

print("\nEscalated Tickets:")
print(df["Escalated"].value_counts())


reopen_rate = (df["Reopened"] == "Yes").mean() * 100
escalation_rate = (df["Escalated"] == "Yes").mean() * 100

print("\nReopen Rate:")
print(f"{reopen_rate:.2f}%")

print("\nEscalation Rate:")
print(f"{escalation_rate:.2f}%")

print("\nSatisfaction Score Distribution:")

print(
    df["Satisfaction_Score"]
    .value_counts()
    .sort_index()
)

avg_satisfaction = df["Satisfaction_Score"].mean()

print("\nAverage Satisfaction Score:")
print(f"{avg_satisfaction:.2f} / 5")

print("\nAverage Satisfaction by Priority:")

satisfaction_by_priority = (
    df.groupby("Priority")["Satisfaction_Score"]
    .mean()
    .sort_values(ascending=False)
)

print(satisfaction_by_priority.round(2))

print("\nAverage Satisfaction by Ticket Status:")

satisfaction_by_status = (
    df.groupby("Ticket_Status")["Satisfaction_Score"]
    .mean()
    .sort_values(ascending=False)
)

print(satisfaction_by_status.round(2))

print("\nAverage Satisfaction by Resolution Time:")

df["Resolution_Time_Group"] = pd.cut(
    df["Resolution_Time_Hours"],
    bins=[0, 4, 8, 12, 24, float("inf")],
    labels=["0-4 hrs", "4-8 hrs", "8-12 hrs", "12-24 hrs", "24+ hrs"]
)

satisfaction_by_resolution = (
    df.groupby("Resolution_Time_Group", observed=True)["Satisfaction_Score"]
    .mean()
)

print(satisfaction_by_resolution.round(2))

print("\nAgent Performance:")

agent_performance = (
    df.groupby("Assigned_Agent")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Avg_Resolution_Hours=("Resolution_Time_Hours", "mean"),
        Avg_Satisfaction=("Satisfaction_Score", "mean")
    )
    .sort_values("Total_Tickets", ascending=False)
)

print(agent_performance.round(2))

print("\nCategory Performance:")

category_performance = (
    df.groupby("Category")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Avg_Resolution_Hours=("Resolution_Time_Hours", "mean"),
        Avg_Satisfaction=("Satisfaction_Score", "mean")
    )
    .sort_values("Total_Tickets", ascending=False)
)

print(category_performance.round(2))

print("\nSLA Performance by Priority:")

sla_by_priority = (
    df[df["SLA_Status"].isin(["Met", "Breached"])]
    .groupby("Priority")["SLA_Status"]
    .value_counts()
    .unstack(fill_value=0)
)

sla_by_priority["Compliance_%"] = (
    sla_by_priority["Met"]
    / (sla_by_priority["Met"] + sla_by_priority["Breached"])
    * 100
)

print(sla_by_priority.round(2))

print("\nSLA Performance by Category:")

sla_by_category = (
    df[df["SLA_Status"].isin(["Met", "Breached"])]
    .groupby("Category")["SLA_Status"]
    .value_counts()
    .unstack(fill_value=0)
)

sla_by_category["Compliance_%"] = (
    sla_by_category["Met"]
    / (sla_by_category["Met"] + sla_by_category["Breached"])
    * 100
)

print(sla_by_category.round(2))

print("\nSupport Level Performance:")

support_performance = (
    df.groupby("Support_Level")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Avg_Resolution_Hours=("Resolution_Time_Hours", "mean"),
        Avg_Satisfaction=("Satisfaction_Score", "mean"),
        Escalated_Tickets=("Escalated", lambda x: (x == "Yes").sum())
    )
)

print(support_performance.round(2))

print("\nTop Issue Types:")

top_issues = (
    df["Issue_Type"]
    .value_counts()
    .head(15)
)

print(top_issues)


# ============================================================
# STEP 32 — Reopened Tickets by Category
# ============================================================

print("\n" + "=" * 60)
print("REOPENED TICKETS BY CATEGORY")
print("=" * 60)

reopened_by_category = (
    df[df["Reopened"] == "Yes"]["Category"]
    .value_counts()
)

print(reopened_by_category)


# ============================================================
# STEP 33 — Reopened Ticket Rate by Category
# ============================================================

print("\n" + "=" * 60)
print("REOPEN RATE BY CATEGORY")
print("=" * 60)

reopen_rate_by_category = (
    df.groupby("Category")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Reopened_Tickets=("Reopened", lambda x: (x == "Yes").sum())
    )
)

reopen_rate_by_category["Reopen_Rate_%"] = (
    reopen_rate_by_category["Reopened_Tickets"]
    / reopen_rate_by_category["Total_Tickets"]
    * 100
)

print(reopen_rate_by_category.round(2))


# ============================================================
# STEP 34 — Escalated Tickets by Category
# ============================================================

print("\n" + "=" * 60)
print("ESCALATED TICKETS BY CATEGORY")
print("=" * 60)

escalated_by_category = (
    df[df["Escalated"] == "Yes"]["Category"]
    .value_counts()
)

print(escalated_by_category)


# ============================================================
# STEP 35 — Escalation Rate by Category
# ============================================================

print("\n" + "=" * 60)
print("ESCALATION RATE BY CATEGORY")
print("=" * 60)

escalation_rate_by_category = (
    df.groupby("Category")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Escalated_Tickets=("Escalated", lambda x: (x == "Yes").sum())
    )
)

escalation_rate_by_category["Escalation_Rate_%"] = (
    escalation_rate_by_category["Escalated_Tickets"]
    / escalation_rate_by_category["Total_Tickets"]
    * 100
)

print(escalation_rate_by_category.round(2))


# ============================================================
# STEP 36 — Resolution Type Analysis
# ============================================================

print("\n" + "=" * 60)
print("RESOLUTION TYPE ANALYSIS")
print("=" * 60)

resolution_type_analysis = (
    df.groupby("Resolution_Type")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Avg_Resolution_Hours=("Resolution_Time_Hours", "mean"),
        Avg_Satisfaction=("Satisfaction_Score", "mean")
    )
    .sort_values("Total_Tickets", ascending=False)
)

print(resolution_type_analysis.round(2))


# ============================================================
# STEP 37 — Location Analysis
# ============================================================

print("\n" + "=" * 60)
print("LOCATION ANALYSIS")
print("=" * 60)

location_analysis = (
    df.groupby("Location")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Avg_Resolution_Hours=("Resolution_Time_Hours", "mean"),
        Avg_Satisfaction=("Satisfaction_Score", "mean")
    )
    .sort_values("Total_Tickets", ascending=False)
)

print(location_analysis.round(2))


# ============================================================
# STEP 38 — Department Performance
# ============================================================

print("\n" + "=" * 60)
print("DEPARTMENT PERFORMANCE")
print("=" * 60)

department_analysis = (
    df.groupby("Department")
    .agg(
        Total_Tickets=("Ticket_ID", "count"),
        Avg_Resolution_Hours=("Resolution_Time_Hours", "mean"),
        Avg_Satisfaction=("Satisfaction_Score", "mean"),
        Escalated_Tickets=("Escalated", lambda x: (x == "Yes").sum()),
        Reopened_Tickets=("Reopened", lambda x: (x == "Yes").sum())
    )
    .sort_values("Total_Tickets", ascending=False)
)

print(department_analysis.round(2))


# ============================================================
# STEP 39 — Priority and Category Combination
# ============================================================

print("\n" + "=" * 60)
print("TICKETS BY PRIORITY AND CATEGORY")
print("=" * 60)

priority_category = pd.crosstab(
    df["Category"],
    df["Priority"]
)

print(priority_category)


# ============================================================
# STEP 40 — Final EDA Summary
# ============================================================

print("\n" + "=" * 60)
print("FINAL EDA SUMMARY")
print("=" * 60)

total_tickets = len(df)

closed_tickets = (
    df["Ticket_Status"] == "Closed"
).sum()

avg_resolution = df["Resolution_Time_Hours"].mean()

avg_satisfaction = df["Satisfaction_Score"].mean()

sla_closed = df[
    df["SLA_Status"].isin(["Met", "Breached"])
]

sla_compliance = (
    (sla_closed["SLA_Status"] == "Met").mean()
    * 100
)

reopen_rate = (
    (df["Reopened"] == "Yes").mean()
    * 100
)

escalation_rate = (
    (df["Escalated"] == "Yes").mean()
    * 100
)

print(f"Total Tickets           : {total_tickets}")
print(f"Closed Tickets          : {closed_tickets}")
print(f"Average Resolution      : {avg_resolution:.2f} hours")
print(f"Average Satisfaction    : {avg_satisfaction:.2f} / 5")
print(f"SLA Compliance          : {sla_compliance:.2f}%")
print(f"Reopen Rate             : {reopen_rate:.2f}%")
print(f"Escalation Rate         : {escalation_rate:.2f}%")


# ============================================================

