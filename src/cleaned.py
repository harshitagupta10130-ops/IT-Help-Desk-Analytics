from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "helpdesk_tickets_raw.csv"

df = pd.read_csv(RAW_FILE)
print(df.shape)
print(df.head().to_string())

print("\nMissing values:")
print(df.isnull().sum())
missing_check = df[
    df["Closed_DateTime"].isna()
]

print("\nTickets with missing Closed_DateTime:")
print(missing_check["Ticket_Status"].value_counts())

print("\nMissing values by ticket status:")

print(
    df.groupby("Ticket_Status")[
        [
            "Closed_DateTime",
            "Resolution_Time_Hours",
            "Satisfaction_Score"
        ]
    ].apply(lambda x: x.isna().sum())
)

print("\nDuplicate Ticket IDs:")
print(df["Ticket_ID"].duplicated().sum())

print("\nPriority values:")
print(df["Priority"].value_counts())

print("\nTicket Status values:")
print(df["Ticket_Status"].value_counts())

print("\nCategory values:")
print(df["Category"].value_counts())

print("\nNumeric column statistics:")

print(
    df[
        [
            "First_Response_Minutes",
            "Resolution_Time_Hours",
            "SLA_Hours",
            "Satisfaction_Score"
        ]
    ].describe()
)

print("\nNegative First Response Times:")
print(
    (df["First_Response_Minutes"] < 0).sum()
)

print("\nNegative Resolution Times:")
print(
    (df["Resolution_Time_Hours"] < 0).sum()
)

print("\nNegative SLA Hours:")
print(
    (df["SLA_Hours"] < 0).sum()
)

print("\nDate column data types:")

print(df[
    [
        "Created_DateTime",
        "Closed_DateTime"
    ]
].dtypes)

df["Created_DateTime"] = pd.to_datetime(
    df["Created_DateTime"],
    errors="coerce"
)

df["Closed_DateTime"] = pd.to_datetime(
    df["Closed_DateTime"],
    errors="coerce"
)

print("\nInvalid Created_DateTime values:")
print(df["Created_DateTime"].isna().sum())

print("\nInvalid Closed_DateTime values:")
print(df["Closed_DateTime"].isna().sum())

print("\nCreated date range:")

print("Earliest:",
      df["Created_DateTime"].min())

print("Latest:",
      df["Created_DateTime"].max())

invalid_dates = df[
    df["Closed_DateTime"].notna()
    &
    (df["Closed_DateTime"] < df["Created_DateTime"])
]

print("\nTickets closed before they were created:")
print(len(invalid_dates))

closed_tickets = df[
    df["Closed_DateTime"].notna()
].copy()

closed_tickets["Calculated_Resolution_Hours"] = (
    closed_tickets["Closed_DateTime"]
    - closed_tickets["Created_DateTime"]
).dt.total_seconds() / 3600


print(
    closed_tickets[
        [
            "Ticket_ID",
            "Resolution_Time_Hours",
            "Calculated_Resolution_Hours"
        ]
    ].head(10)
)

print(
    df[
        [
            "Ticket_ID",
            "Ticket_Status",
            "Resolution_Time_Hours",
            "SLA_Hours",
            "SLA_Status"
        ]
    ].head(10).to_string(index=False)
)

closed_tickets = df[df["Ticket_Status"] == "Closed"].copy()

closed_tickets["Expected_SLA_Status"] = (
    closed_tickets["Resolution_Time_Hours"]
    <= closed_tickets["SLA_Hours"]
).map({
    True: "Met",
    False: "Breached"
})

sla_errors = closed_tickets[
    closed_tickets["SLA_Status"] != closed_tickets["Expected_SLA_Status"]
]

print("\nIncorrect SLA records:")
print(len(sla_errors))

print("\nEscalated values:")
print(df["Escalated"].value_counts())

print("\nReopened values:")
print(df["Reopened"].value_counts())


valid_values = {"Yes", "No"}

invalid_escalated = df[
    ~df["Escalated"].isin(valid_values)
]

invalid_reopened = df[
    ~df["Reopened"].isin(valid_values)
]

print("\nInvalid Escalated values:")
print(len(invalid_escalated))

print("\nInvalid Reopened values:")
print(len(invalid_reopened))

invalid_reopened_status = df[
    (df["Reopened"] == "Yes") &
    (df["Ticket_Status"] != "Closed")
]

print("\nReopened tickets that are not Closed:")
print(len(invalid_reopened_status))

# Step 8: Final cleaning

text_columns = [
    "Ticket_ID",
    "Employee_ID",
    "Department",
    "Location",
    "Assigned_Agent",
    "Support_Level",
    "Ticket_Status",
    "Priority",
    "Category",
    "Subcategory",
    "Issue_Type",
    "Resolution_Type",
    "Escalated",
    "Reopened",
    "SLA_Status"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

print("\nFinal dataset shape:")
print(df.shape)

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

CLEANED_FILE = PROCESSED_DIR / "helpdesk_tickets_cleaned.csv"

df.to_csv(CLEANED_FILE, index=False)

print("\nCleaned dataset saved to:")
print(CLEANED_FILE)

# Step 9: Final data quality check

print("\n" + "=" * 40)
print("FINAL DATA QUALITY CHECK")
print("=" * 40)

print("\nDataset shape:")
print(df.shape)

print("\nDuplicate Ticket IDs:")
print(df["Ticket_ID"].duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDate range:")
print("Start:", df["Created_DateTime"].min())
print("End:", df["Created_DateTime"].max())

print("\nTicket status:")
print(df["Ticket_Status"].value_counts())

print("\nPriority:")
print(df["Priority"].value_counts())

print("\nCategory:")
print(df["Category"].value_counts())