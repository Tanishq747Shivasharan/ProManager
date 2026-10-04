import pandas as pd 
 
# Load dataset 
df = pd.read_csv("../data/IT_Project_Delay.csv") 
 
# Display first 5 records 
print(df.head()) 
 
# Display dataset information 
print(df.info())

# Number of rows and columns 
print("Dataset Shape:") 
print(df.shape) 
 
# Column names 
print("\nColumn Names:") 
print(df.columns) 
 
# Check missing values 
print("\nMissing Values:") 
print(df.isnull().sum()) 
 
# Check duplicate rows 
print("\nDuplicate Rows:") 
print(df.duplicated().sum()) 
 
# Statistical summary 
print("\nStatistical Summary:") 
print(df.describe()) 
 
# ---------------- DATA CLEANING ---------------- 
 
# Remove duplicate rows 
df = df.drop_duplicates() 
 
# Check missing values 
print("\nMissing Values After Cleaning:") 
print(df.isnull().sum()) 
 
# Check data types 
print("\nData Types:") 
print(df.dtypes) 
 
# Check negative values in important columns 
print("\nNegative Delay Days:") 
print((df["Delay_Days"] < 0).sum()) 
 
print("\nNegative Team Size:") 
print((df["Team_Size"] < 0).sum()) 

# ---------------- DATA CONSISTENCY CHECK ---------------- 
 
# Calculate Delay Days 
df["Delay_Days"] = df["Actual_Days"] - df["Planned_Days"] 
 
# Calculate Cost Overrun 
df["Cost_Overrun"] = df["Actual_Cost"] - df["Budget"] 
 
# Check project status 
print("\nProject Status:") 
print(df["Project_Status"].value_counts()) 
 
# Check delay reasons 
print("\nDelay Reasons:") 
print(df["Delay_Reason"].value_counts()) 
 
# Check calculated values 
print("\nDelay and Cost Overrun:") 
print(df[[ 
    "Project_ID", 
    "Planned_Days", 
    "Actual_Days", 
    "Delay_Days", 
    "Budget", 
    "Actual_Cost", 
    "Cost_Overrun" 
]].head()) 

# ---------------- KPI ANALYSIS ---------------- 
 
# Total projects 
total_projects = len(df) 
 
# Delayed projects 
delayed_projects = (df["Delay_Days"] > 0).sum() 
 
# On-time projects 
on_time_projects = (df["Delay_Days"] == 0).sum() 
 
# Average delay 
average_delay = df["Delay_Days"].mean() 
 
# Total cost overrun 
total_cost_overrun = df["Cost_Overrun"].sum() 
 
print("\n========== PROJECT KPIs ==========") 
print("Total Projects:", total_projects) 
print("Delayed Projects:", delayed_projects) 
print("On-Time Projects:", on_time_projects) 
print("Average Delay:", round(average_delay, 2), "days") 
print("Total Cost Overrun: ₹", total_cost_overrun) 

# ---------------- DEPARTMENT-WISE ANALYSIS ---------------- 
 
department_analysis = df.groupby("Department").agg( 
    Total_Projects=("Project_ID", "count"), 
    Delayed_Projects=("Delay_Days", lambda x: (x > 0).sum()), 
    Average_Delay=("Delay_Days", "mean"), 
    Average_Bugs=("Bugs_Count", "mean"), 
    Average_Satisfaction=("Customer_Satisfaction", "mean") 
).reset_index() 
 
print("\n========== DEPARTMENT-WISE ANALYSIS ==========") 
print(department_analysis) 

# ---------------- DELAY REASON ANALYSIS ---------------- 
 
delay_reason_analysis = df.groupby("Delay_Reason").agg( 
    Total_Projects=("Project_ID", "count"), 
    Average_Delay=("Delay_Days", "mean"), 
    Average_Bugs=("Bugs_Count", "mean"), 
    Average_Client_Changes=("Client_Changes", "mean") 
).reset_index() 
 
print("\n========== DELAY REASON ANALYSIS ==========") 
print(delay_reason_analysis.sort_values("Average_Delay", ascending=False)) 

# ---------------- TEAM EXPERIENCE ANALYSIS ---------------- 
 
experience_analysis = df.groupby("Team_Experience").agg( 
    Total_Projects=("Project_ID", "count"), 
    Delayed_Projects=("Delay_Days", lambda x: (x > 0).sum()), 
    Average_Delay=("Delay_Days", "mean"), 
    Average_Bugs=("Bugs_Count", "mean"), 
    Average_Satisfaction=("Customer_Satisfaction", "mean") 
).reset_index() 
 
print("\n========== TEAM EXPERIENCE ANALYSIS ==========") 
print( 
    experience_analysis.sort_values( 
        "Average_Delay", 
        ascending=False 
    ) 
) 

# ---------------- CLIENT CHANGES ANALYSIS ---------------- 
 
client_changes_analysis = df.groupby("Client_Changes").agg( 
    Total_Projects=("Project_ID", "count"), 
    Average_Delay=("Delay_Days", "mean"), 
    Delayed_Projects=("Delay_Days", lambda x: (x > 0).sum()), 
    Average_Bugs=("Bugs_Count", "mean"), 
    Average_Satisfaction=("Customer_Satisfaction", "mean") 
).reset_index() 
 
print("\n========== CLIENT CHANGES ANALYSIS ==========") 
print(client_changes_analysis.sort_values("Client_Changes")) 

# ---------------- BUGS ANALYSIS ---------------- 
 
bugs_analysis = df.groupby("Bugs_Count").agg( 
    Total_Projects=("Project_ID", "count"), 
    Average_Delay=("Delay_Days", "mean"), 
    Average_Cost_Overrun=("Cost_Overrun", "mean"), 
    Average_Satisfaction=("Customer_Satisfaction", "mean") 
).reset_index() 
 
print("\n========== BUGS ANALYSIS ==========") 
print(bugs_analysis.sort_values("Bugs_Count")) 

# ---------------- COST ANALYSIS ---------------- 
 
cost_analysis = df.groupby("Department").agg( 
    Total_Projects=("Project_ID", "count"), 
    Total_Budget=("Budget", "sum"), 
    Total_Actual_Cost=("Actual_Cost", "sum"), 
    Total_Cost_Overrun=("Cost_Overrun", "sum"), 
    Average_Cost_Overrun=("Cost_Overrun", "mean") 
).reset_index() 
 
print("\n========== COST ANALYSIS ==========") 
print(cost_analysis.sort_values("Total_Cost_Overrun", ascending=False)) 

# ---------------- CUSTOMER SATISFACTION ANALYSIS ---------------- 
 
satisfaction_analysis = df.groupby("Project_Status").agg( 
    Total_Projects=("Project_ID", "count"), 
    Average_Delay=("Delay_Days", "mean"), 
    Average_Satisfaction=("Customer_Satisfaction", "mean"), 
    Average_Bugs=("Bugs_Count", "mean"), 
    Average_Cost_Overrun=("Cost_Overrun", "mean") 
).reset_index() 
 
print("\n========== CUSTOMER SATISFACTION ANALYSIS ==========") 
print(satisfaction_analysis)