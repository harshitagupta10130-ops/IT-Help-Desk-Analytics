USE IT_HelpDesk;

-- ============================================================
-- IT HELP DESK ANALYTICS PROJECT
-- SQL ANALYSIS
-- ============================================================


-- ============================================================
-- 1. CHECK TOTAL RECORDS
-- ============================================================

SELECT COUNT(*) AS Total_Tickets
FROM helpdesk_tickets;


-- ============================================================
-- 2. OVERALL KPI ANALYSIS
-- ============================================================

SELECT
    COUNT(*) AS Total_Tickets,

    SUM(Ticket_Status = 'Closed') AS Closed_Tickets,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets;


-- ============================================================
-- 3. TICKET STATUS DISTRIBUTION
-- ============================================================

SELECT
    Ticket_Status,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Ticket_Status
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 4. SLA PERFORMANCE
-- ============================================================

SELECT
    COUNT(*) AS Applicable_Tickets,

    SUM(SLA_Status = 'Met') AS SLA_Met,

    SUM(SLA_Status = 'Breached') AS SLA_Breached,

    ROUND(
        SUM(SLA_Status = 'Met') /
        COUNT(*) * 100,
        2
    ) AS SLA_Compliance_Percent

FROM helpdesk_tickets

WHERE SLA_Status IN ('Met', 'Breached');


-- ============================================================
-- 5. SLA STATUS DISTRIBUTION
-- ============================================================

SELECT
    SLA_Status,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY SLA_Status
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 6. REOPEN RATE
-- ============================================================

SELECT
    COUNT(*) AS Total_Tickets,

    SUM(Reopened = 'Yes') AS Reopened_Tickets,

    ROUND(
        SUM(Reopened = 'Yes') /
        COUNT(*) * 100,
        2
    ) AS Reopen_Rate_Percent

FROM helpdesk_tickets;


-- ============================================================
-- 7. ESCALATION RATE
-- ============================================================

SELECT
    COUNT(*) AS Total_Tickets,

    SUM(Escalated = 'Yes') AS Escalated_Tickets,

    ROUND(
        SUM(Escalated = 'Yes') /
        COUNT(*) * 100,
        2
    ) AS Escalation_Rate_Percent

FROM helpdesk_tickets;


-- ============================================================
-- 8. TICKET VOLUME BY CATEGORY
-- ============================================================

SELECT
    Category,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Category
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 9. CATEGORY PERFORMANCE
-- ============================================================

SELECT
    Category,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets

GROUP BY Category

ORDER BY Ticket_Count DESC;


-- ============================================================
-- 10. PRIORITY-WISE TICKET VOLUME
-- ============================================================

SELECT
    Priority,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Priority
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 11. SLA COMPLIANCE BY PRIORITY
-- ============================================================

SELECT
    Priority,

    COUNT(*) AS Applicable_Tickets,

    SUM(SLA_Status = 'Met') AS SLA_Met,

    SUM(SLA_Status = 'Breached') AS SLA_Breached,

    ROUND(
        SUM(SLA_Status = 'Met') /
        COUNT(*) * 100,
        2
    ) AS SLA_Compliance_Percent

FROM helpdesk_tickets

WHERE SLA_Status IN ('Met', 'Breached')

GROUP BY Priority

ORDER BY SLA_Compliance_Percent DESC;


-- ============================================================
-- 12. SUPPORT LEVEL PERFORMANCE
-- ============================================================

SELECT
    Support_Level,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction,

    SUM(Escalated = 'Yes') AS Escalated_Tickets

FROM helpdesk_tickets

GROUP BY Support_Level

ORDER BY Support_Level;


-- ============================================================
-- 13. TICKET VOLUME BY DEPARTMENT
-- ============================================================

SELECT
    Department,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Department
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 14. TICKET VOLUME BY LOCATION
-- ============================================================

SELECT
    Location,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Location
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 15. TICKET VOLUME BY MONTH
-- ============================================================

SELECT
    Month,
    Month_Name,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY
    Month,
    Month_Name
ORDER BY Month;


-- ============================================================
-- 16. TICKET VOLUME BY DAY OF WEEK
-- ============================================================

SELECT
    Day_of_Week,
    Day_Name,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY
    Day_of_Week,
    Day_Name
ORDER BY Day_of_Week;


-- ============================================================
-- 17. TICKET VOLUME BY HOUR
-- ============================================================

SELECT
    Created_Hour,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Created_Hour
ORDER BY Created_Hour;


-- ============================================================
-- 18. WEEKDAY VS WEEKEND
-- ============================================================

SELECT
    Is_Weekend,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Is_Weekend
ORDER BY Is_Weekend;


-- ============================================================
-- 19. ISSUE TYPE ANALYSIS
-- ============================================================

SELECT
    Issue_Type,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Issue_Type
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 20. RESOLUTION TYPE ANALYSIS
-- ============================================================

SELECT
    Resolution_Type,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Resolution_Type
ORDER BY Ticket_Count DESC;


-- ============================================================
-- 21. SATISFACTION BY PRIORITY
-- ============================================================

SELECT
    Priority,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets

GROUP BY Priority

ORDER BY Avg_Satisfaction DESC;


-- ============================================================
-- 22. SATISFACTION BY SUPPORT LEVEL
-- ============================================================

SELECT
    Support_Level,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets

GROUP BY Support_Level

ORDER BY Support_Level;


-- ============================================================
-- 23. REOPENED TICKETS ANALYSIS
-- ============================================================

SELECT
    Reopened,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Reopened;


-- ============================================================
-- 24. ESCALATED TICKETS ANALYSIS
-- ============================================================

SELECT
    Escalated,
    COUNT(*) AS Ticket_Count
FROM helpdesk_tickets
GROUP BY Escalated;


-- ============================================================
-- 25. AVERAGE RESOLUTION BY PRIORITY
-- ============================================================

SELECT
    Priority,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours

FROM helpdesk_tickets

GROUP BY Priority

ORDER BY Avg_Resolution_Hours DESC;


-- ============================================================
-- 26. RESOLUTION TIME VS SATISFACTION
-- ============================================================

SELECT
    CASE
        WHEN Resolution_Time_Hours <= 4
            THEN '0-4 Hours'

        WHEN Resolution_Time_Hours <= 8
            THEN '4-8 Hours'

        WHEN Resolution_Time_Hours <= 12
            THEN '8-12 Hours'

        WHEN Resolution_Time_Hours <= 24
            THEN '12-24 Hours'

        ELSE '24+ Hours'
    END AS Resolution_Bucket,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets

WHERE Resolution_Time_Hours IS NOT NULL

GROUP BY Resolution_Bucket

ORDER BY
    CASE Resolution_Bucket
        WHEN '0-4 Hours' THEN 1
        WHEN '4-8 Hours' THEN 2
        WHEN '8-12 Hours' THEN 3
        WHEN '12-24 Hours' THEN 4
        WHEN '24+ Hours' THEN 5
    END;


-- ============================================================
-- 27. CATEGORY + PRIORITY ANALYSIS
-- ============================================================

SELECT
    Category,
    Priority,
    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets

GROUP BY
    Category,
    Priority

ORDER BY
    Category,
    Ticket_Count DESC;


-- ============================================================
-- 28. CATEGORY + SLA ANALYSIS
-- ============================================================

SELECT
    Category,

    COUNT(*) AS Applicable_Tickets,

    SUM(SLA_Status = 'Met') AS SLA_Met,

    SUM(SLA_Status = 'Breached') AS SLA_Breached,

    ROUND(
        SUM(SLA_Status = 'Met') /
        COUNT(*) * 100,
        2
    ) AS SLA_Compliance_Percent

FROM helpdesk_tickets

WHERE SLA_Status IN ('Met', 'Breached')

GROUP BY Category

ORDER BY SLA_Compliance_Percent DESC;


-- ============================================================
-- 29. DEPARTMENT PERFORMANCE
-- ============================================================

SELECT
    Department,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction

FROM helpdesk_tickets

GROUP BY Department

ORDER BY Ticket_Count DESC;


-- ============================================================
-- 30. AGENT PERFORMANCE
-- ============================================================

SELECT
    Assigned_Agent,

    COUNT(*) AS Ticket_Count,

    ROUND(
        AVG(Resolution_Time_Hours),
        2
    ) AS Avg_Resolution_Hours,

    ROUND(
        AVG(Satisfaction_Score),
        2
    ) AS Avg_Satisfaction,

    SUM(Escalated = 'Yes') AS Escalated_Tickets

FROM helpdesk_tickets

GROUP BY Assigned_Agent

ORDER BY Ticket_Count DESC;