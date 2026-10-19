from pathlib import Path
import numpy as np
import pandas as pd


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

RANDOM_SEED = 42
N_TICKETS = 5_000

START_DATE = "2025-01-01"
END_DATE = "2026-08-31"

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

CSV_PATH = RAW_DATA_DIR / "helpdesk_tickets_raw.csv"
EXCEL_PATH = RAW_DATA_DIR / "helpdesk_tickets_raw.xlsx"

rng = np.random.default_rng(RANDOM_SEED)


# ============================================================
# MASTER DATA
# ============================================================

DEPARTMENTS = {
    "IT": 0.08,
    "HR": 0.08,
    "Finance": 0.12,
    "Sales": 0.15,
    "Marketing": 0.08,
    "Operations": 0.13,
    "Management": 0.05,
    "Customer Support": 0.12,
    "Administration": 0.08,
    "Engineering": 0.07,
    "Procurement": 0.02,
    "Legal": 0.02,
}


LOCATIONS = {
    "Lucknow": 0.40,
    "Noida": 0.18,
    "Delhi": 0.15,
    "Bangalore": 0.12,
    "Mumbai": 0.08,
    "Hyderabad": 0.07,
}


AGENTS = [
    f"Agent_{number:02d}"
    for number in range(1, 21)
]


CATEGORIES = {
    "Hardware": {
        "weight": 0.15,
        "subcategories": [
            "Laptop",
            "Desktop",
            "Monitor",
            "Keyboard",
            "Mouse",
            "Docking Station",
        ],
        "issues": [
            "Device Not Working",
            "Hardware Failure",
            "Slow Device",
            "Peripheral Not Detected",
        ],
    },

    "Software": {
        "weight": 0.16,
        "subcategories": [
            "Windows",
            "Microsoft Office",
            "Browser",
            "Business Application",
            "Antivirus",
        ],
        "issues": [
            "Application Crash",
            "Installation Error",
            "Software Not Responding",
            "Update Failure",
            "License Issue",
        ],
    },

    "Network": {
        "weight": 0.18,
        "subcategories": [
            "Wi-Fi",
            "VPN",
            "Internet",
            "LAN",
            "DNS",
        ],
        "issues": [
            "Connection Failure",
            "Slow Network",
            "VPN Connection Failed",
            "Intermittent Connection",
            "No Internet Access",
        ],
    },

    "Access": {
        "weight": 0.15,
        "subcategories": [
            "Password Reset",
            "Account Lock",
            "Permission",
            "New Account",
            "System Access",
        ],
        "issues": [
            "Password Reset Required",
            "Account Locked",
            "Access Denied",
            "New User Access",
            "Permission Request",
        ],
    },

    "Security": {
        "weight": 0.07,
        "subcategories": [
            "Phishing",
            "Malware",
            "Endpoint Security",
            "Security Alert",
        ],
        "issues": [
            "Suspicious Email",
            "Malware Alert",
            "Security Warning",
            "Unauthorized Activity",
        ],
    },

    "Email": {
        "weight": 0.12,
        "subcategories": [
            "Outlook",
            "Email Login",
            "Email Delivery",
            "Mailbox",
            "Spam",
        ],
        "issues": [
            "Email Not Sending",
            "Email Not Receiving",
            "Login Failure",
            "Mailbox Full",
            "Spam Issue",
        ],
    },

    "Printer": {
        "weight": 0.09,
        "subcategories": [
            "Paper Jam",
            "Printing Error",
            "Network Printer",
            "Driver",
        ],
        "issues": [
            "Printer Not Working",
            "Paper Jam",
            "Print Quality Issue",
            "Printer Offline",
            "Driver Error",
        ],
    },

    "Other": {
        "weight": 0.08,
        "subcategories": [
            "General Request",
            "Information",
            "IT Consultation",
        ],
        "issues": [
            "General IT Request",
            "Technical Assistance",
            "Information Request",
        ],
    },
}


PRIORITIES = {
    "Low": {
        "weight": 0.30,
        "sla_hours": 24,
        "response_range": (30, 240),
        "resolution_range": (2, 36),
    },

    "Medium": {
        "weight": 0.45,
        "sla_hours": 12,
        "response_range": (15, 120),
        "resolution_range": (1, 20),
    },

    "High": {
        "weight": 0.20,
        "sla_hours": 8,
        "response_range": (5, 60),
        "resolution_range": (0.5, 12),
    },

    "Critical": {
        "weight": 0.05,
        "sla_hours": 4,
        "response_range": (1, 30),
        "resolution_range": (0.25, 8),
    },
}


TICKET_STATUSES = {
    "Closed": 0.76,
    "In Progress": 0.08,
    "Pending": 0.08,
    "Open": 0.06,
    "Cancelled": 0.02,
}


RESOLUTION_TYPES = {
    "Remote": 0.60,
    "Onsite": 0.22,
    "Knowledge Base": 0.08,
    "Vendor": 0.05,
    "Escalation": 0.05,
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def weighted_choice(mapping):
    """Select one item using probability weights."""

    items = list(mapping.keys())
    weights = np.array(
        list(mapping.values()),
        dtype=float
    )

    weights = weights / weights.sum()

    return rng.choice(items, p=weights)


def choose_category():

    weights = {
        category: details["weight"]
        for category, details in CATEGORIES.items()
    }

    return weighted_choice(weights)


def choose_priority():

    weights = {
        priority: details["weight"]
        for priority, details in PRIORITIES.items()
    }

    return weighted_choice(weights)


def generate_created_datetime():

    start = pd.Timestamp(START_DATE)
    end = pd.Timestamp(END_DATE)

    total_days = (end - start).days

    random_day = int(
        rng.integers(
            0,
            total_days + 1
        )
    )

    date = start + pd.Timedelta(
        days=random_day
    )

    # Business hours receive more tickets.
    hours = np.arange(7, 23)

    probabilities = np.array([
        0.02, 0.03, 0.10, 0.12,
        0.12, 0.10, 0.09, 0.10,
        0.10, 0.07, 0.05, 0.04,
        0.03, 0.02, 0.01, 0.00
    ])

    probabilities = probabilities / probabilities.sum()

    hour = int(
        rng.choice(
            hours,
            p=probabilities
        )
    )

    minute = int(
        rng.integers(0, 60)
    )

    second = int(
        rng.integers(0, 60)
    )

    return date.replace(
        hour=hour,
        minute=minute,
        second=second
    )


def choose_support_level(priority):

    if priority == "Critical":

        return rng.choice(
            ["L1", "L2", "L3"],
            p=[0.10, 0.35, 0.55]
        )

    if priority == "High":

        return rng.choice(
            ["L1", "L2", "L3"],
            p=[0.35, 0.50, 0.15]
        )

    return rng.choice(
        ["L1", "L2", "L3"],
        p=[0.70, 0.25, 0.05]
    )


def generate_response_time(priority):

    minimum, maximum = PRIORITIES[
        priority
    ]["response_range"]

    response_time = rng.uniform(
        minimum,
        maximum
    )

    return round(
        max(response_time, 1),
        2
    )


def generate_resolution_time(
    priority,
    category
):

    minimum, maximum = PRIORITIES[
        priority
    ]["resolution_range"]

    resolution_time = rng.uniform(
        minimum,
        maximum
    )

    category_multiplier = {
        "Hardware": 1.20,
        "Software": 1.10,
        "Network": 1.25,
        "Access": 0.70,
        "Security": 1.30,
        "Email": 0.85,
        "Printer": 1.05,
        "Other": 0.90,
    }

    resolution_time *= category_multiplier[
        category
    ]

    return round(
        max(resolution_time, 0.25),
        2
    )


def calculate_satisfaction(
    resolution_time,
    reopened,
    escalated
):

    score = 5.0

    if resolution_time > 24:
        score -= 1.2

    elif resolution_time > 12:
        score -= 0.7

    elif resolution_time > 6:
        score -= 0.3

    if reopened == "Yes":
        score -= 0.7

    if escalated == "Yes":
        score -= 0.3

    # Natural variation in user feedback.
    score += rng.normal(
        0,
        0.35
    )

    score = np.clip(
        score,
        1,
        5
    )

    return int(
        round(score)
    )


# ============================================================
# GENERATE DATA
# ============================================================

print("=" * 60)
print("IT HELP DESK DATASET GENERATOR")
print("=" * 60)

records = []


for ticket_number in range(
    1,
    N_TICKETS + 1
):

    ticket_id = (
        f"HD{ticket_number:05d}"
    )

    created_datetime = (
        generate_created_datetime()
    )

    category = choose_category()

    subcategory = rng.choice(
        CATEGORIES[
            category
        ]["subcategories"]
    )

    issue_type = rng.choice(
        CATEGORIES[
            category
        ]["issues"]
    )

    priority = choose_priority()

    department = weighted_choice(
        DEPARTMENTS
    )

    location = weighted_choice(
        LOCATIONS
    )

    employee_id = (
        f"EMP{int(rng.integers(1000, 9999))}"
    )

    assigned_agent = rng.choice(
        AGENTS
    )

    support_level = (
        choose_support_level(
            priority
        )
    )

    ticket_status = weighted_choice(
        TICKET_STATUSES
    )

    resolution_type = weighted_choice(
        RESOLUTION_TYPES
    )

    first_response_minutes = (
        generate_response_time(
            priority
        )
    )

    # --------------------------------------------------------
    # Resolution
    # --------------------------------------------------------

    if ticket_status == "Closed":

        resolution_time_hours = (
            generate_resolution_time(
                priority,
                category
            )
        )

        closed_datetime = (
            created_datetime
            + pd.Timedelta(
                hours=float(
                    resolution_time_hours
                )
            )
        )

    else:

        resolution_time_hours = np.nan
        closed_datetime = pd.NaT

    # --------------------------------------------------------
    # SLA
    # --------------------------------------------------------

    sla_hours = PRIORITIES[
        priority
    ]["sla_hours"]

    if pd.isna(
        resolution_time_hours
    ):

        sla_status = "Not Applicable"

    elif (
        resolution_time_hours
        <= sla_hours
    ):

        sla_status = "Met"

    else:

        sla_status = "Breached"

    # --------------------------------------------------------
    # Escalation
    # --------------------------------------------------------

    escalation_probability = {
        "Low": 0.03,
        "Medium": 0.06,
        "High": 0.15,
        "Critical": 0.35,
    }[priority]

    escalated = (
        "Yes"
        if rng.random()
        < escalation_probability
        else "No"
    )

    # --------------------------------------------------------
    # Reopened
    # --------------------------------------------------------

    reopen_probability = {
        "Low": 0.03,
        "Medium": 0.05,
        "High": 0.08,
        "Critical": 0.12,
    }[priority]

    reopened = (
        "Yes"
        if (
            ticket_status == "Closed"
            and rng.random()
            < reopen_probability
        )
        else "No"
    )

    # --------------------------------------------------------
    # Satisfaction
    # --------------------------------------------------------

    if ticket_status == "Closed":

        satisfaction_score = (
            calculate_satisfaction(
                resolution_time_hours,
                reopened,
                escalated
            )
        )

    else:

        satisfaction_score = np.nan

    # --------------------------------------------------------
    # Store record
    # --------------------------------------------------------

    records.append({

        "Ticket_ID": ticket_id,

        "Created_DateTime":
            created_datetime,

        "Closed_DateTime":
            closed_datetime,

        "Employee_ID":
            employee_id,

        "Department":
            department,

        "Location":
            location,

        "Assigned_Agent":
            assigned_agent,

        "Support_Level":
            support_level,

        "Ticket_Status":
            ticket_status,

        "Priority":
            priority,

        "Category":
            category,

        "Subcategory":
            subcategory,

        "Issue_Type":
            issue_type,

        "Resolution_Type":
            resolution_type,

        "Escalated":
            escalated,

        "Reopened":
            reopened,

        "First_Response_Minutes":
            first_response_minutes,

        "Resolution_Time_Hours":
            resolution_time_hours,

        "SLA_Hours":
            sla_hours,

        "SLA_Status":
            sla_status,

        "Satisfaction_Score":
            satisfaction_score,
    })


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(records)


# ============================================================
# DATE FEATURES
# ============================================================

df["Created_DateTime"] = pd.to_datetime(
    df["Created_DateTime"]
)

df["Closed_DateTime"] = pd.to_datetime(
    df["Closed_DateTime"]
)

df["Created_Date"] = (
    df["Created_DateTime"].dt.date
)

df["Created_Time"] = (
    df["Created_DateTime"]
    .dt.strftime("%H:%M:%S")
)

df["Created_Year"] = (
    df["Created_DateTime"].dt.year
)

df["Created_Month"] = (
    df["Created_DateTime"].dt.month
)

df["Month_Name"] = (
    df["Created_DateTime"]
    .dt.month_name()
)

df["Day_Name"] = (
    df["Created_DateTime"]
    .dt.day_name()
)

df["Day_of_Week"] = (
    df["Created_DateTime"]
    .dt.dayofweek
)

df["Created_Hour"] = (
    df["Created_DateTime"].dt.hour
)

df["Is_Weekend"] = np.where(
    df["Day_of_Week"] >= 5,
    "Yes",
    "No"
)


# ============================================================
# SLA FLAG
# ============================================================

df["SLA_Breach_Flag"] = np.where(
    df["SLA_Status"] == "Breached",
    1,
    0
)


# ============================================================
# RESPONSE CATEGORY
# ============================================================

df["Response_Category"] = pd.cut(
    df["First_Response_Minutes"],
    bins=[
        0,
        15,
        30,
        60,
        120,
        np.inf
    ],
    labels=[
        "Very Fast",
        "Fast",
        "Moderate",
        "Slow",
        "Very Slow"
    ],
    include_lowest=True
)


# ============================================================
# DATA QUALITY CHECKS
# ============================================================

print("\nDATASET SUMMARY")
print("-" * 60)

print(
    f"Total tickets: {len(df):,}"
)

print(
    f"Total columns: {len(df.columns)}"
)

print(
    f"Duplicate Ticket IDs: "
    f"{df['Ticket_ID'].duplicated().sum()}"
)

print("\nTicket Status:")
print(
    df["Ticket_Status"]
    .value_counts()
)

print("\nPriority:")
print(
    df["Priority"]
    .value_counts()
)

print("\nCategory:")
print(
    df["Category"]
    .value_counts()
)

print("\nSLA Status:")
print(
    df["SLA_Status"]
    .value_counts()
)


# ============================================================
# SAVE FILES
# ============================================================

df.to_csv(
    CSV_PATH,
    index=False
)

df.to_excel(
    EXCEL_PATH,
    index=False
)


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("DATASET GENERATION COMPLETED SUCCESSFULLY")
print("=" * 60)

print(
    f"CSV: {CSV_PATH}"
)

print(
    f"Excel: {EXCEL_PATH}"
)

print("\nFirst 5 records:")
print(
    df.head().to_string(
        index=False
    )
)