import pandas as pd 
import matplotlib.pyplot as plt 
import os 
 
# Load dataset 
df = pd.read_csv("../data/IT_Project_Delay.csv") 
 
# Create visualization folder 
os.makedirs("../visualizations", exist_ok=True) 
 
 
# ---------------- CHART 1: PROJECTS BY DEPARTMENT ---------------- 
 
department_projects = df["Department"].value_counts() 
 
plt.figure(figsize=(10, 6)) 
department_projects.plot(kind="bar") 
 
plt.title("Number of Projects by Department") 
plt.xlabel("Department") 
plt.ylabel("Number of Projects") 
plt.xticks(rotation=45) 
plt.tight_layout() 
 
plt.savefig("../visualizations/projects_by_department.png") 
plt.show() 
 
 
# ---------------- CHART 2: AVERAGE DELAY BY DEPARTMENT ---------------- 
 
avg_delay_department = df.groupby("Department")["Delay_Days"].mean() 
 
plt.figure(figsize=(10, 6)) 
avg_delay_department.plot(kind="bar") 
 
plt.title("Average Project Delay by Department") 
plt.xlabel("Department") 
plt.ylabel("Average Delay (Days)") 
plt.xticks(rotation=45) 
plt.tight_layout() 
 
plt.savefig("../visualizations/average_delay_by_department.png") 
plt.show() 
 
 
# ---------------- CHART 3: PROJECTS BY DELAY REASON ---------------- 
 
delay_reason_count = df["Delay_Reason"].value_counts() 
 
plt.figure(figsize=(10, 6)) 
delay_reason_count.plot(kind="bar") 
 
plt.title("Projects by Delay Reason") 
plt.xlabel("Delay Reason") 
plt.ylabel("Number of Projects") 
plt.xticks(rotation=45) 
plt.tight_layout() 
 
plt.savefig("../visualizations/projects_by_delay_reason.png") 
plt.show() 
 
 
# ---------------- CHART 4: BUGS VS DELAY ---------------- 
 
plt.figure(figsize=(10, 6)) 
 
plt.scatter( 
    df["Bugs_Count"], 
    df["Delay_Days"] 
) 
 
plt.title("Bugs vs Project Delay") 
plt.xlabel("Number of Bugs") 
plt.ylabel("Delay (Days)") 
plt.tight_layout() 
 
plt.savefig("../visualizations/bugs_vs_delay.png") 
plt.show() 
 
 
# ---------------- CHART 5: PLANNED VS ACTUAL DAYS ---------------- 
 
plt.figure(figsize=(10, 6)) 
 
plt.scatter( 
    df["Planned_Days"], 
    df["Actual_Days"] 
) 
 
plt.title("Planned Days vs Actual Days") 
plt.xlabel("Planned Days") 
plt.ylabel("Actual Days") 
plt.tight_layout() 
 
plt.savefig("../visualizations/planned_vs_actual_days.png") 
plt.show() 
 
print("\nAll charts created successfully!")