# IT Project Delay & Performance Analytics

A data analytics project that finds **why IT projects get delayed and go over budget**, using a synthetic dataset of 250 software projects.

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn

**Question answered:** What factors are associated with IT project delays and cost overruns, and what can management learn from historical project data?

> Note: the data is synthetic (generated with a fixed random seed), so the findings describe this dataset, not real companies.

---

## KPI Summary

| KPI | Value |
|---|---|
| Total projects | 250 |
| Delayed projects | 182 (72.8%) |
| Average delay | 10.1 days |
| Average cost overrun | 9.5% |
| Average task completion | 95.6% |
| Average client satisfaction | 4.1 / 5 |

---

## Key Findings

### 1. ERP and AI/ML projects are delayed the most

Average delay by project type (each `#` = 1 day):

```
ERP     | ########################## 26.5
AI/ML   | #################### 20.5
Cloud   | ########### 11.4
Data    | ######### 9.6
Mobile  | ###### 6.4
Web     | -0.5 (on time)
```

| Project Type | Projects | Avg Delay (days) | Avg Client Changes | Avg Cost Overrun % |
|---|---|---|---|---|
| ERP | 35 | 26.5 | 5.5 | 16.5 |
| AI/ML | 26 | 20.5 | 5.1 | 15.4 |
| Cloud | 34 | 11.4 | 3.9 | 10.1 |
| Data | 43 | 9.6 | 3.7 | 9.7 |
| Mobile | 46 | 6.4 | 3.5 | 6.4 |
| Web | 66 | -0.5 | 2.7 | 5.2 |

The project types with the most delay also get the most client changes and have the highest cost overruns.

### 2. More client changes means longer delays

Average delay by number of client changes (each `#` = 1 day):

```
Low (0-2 changes)      | ## 1.9
Medium (3-5 changes)   | ############ 12.1
High (6+ changes)      | ################# 17.3
```

Projects with 6 or more client changes are delayed about 9 times longer than projects with 0 to 2 changes.

### 3. More bugs are associated with longer delays

Bugs found and delay have a positive correlation (r = 0.37), similar in strength to client changes (r = 0.38).

### 4. Smaller teams are delayed slightly more

Average delay by team size (each `#` = 1 day):

```
Small (5 or fewer)   | ############ 12.1
Medium (6-10)        | ########## 10.5
Large (11+)          | ######## 8.0
```

The overall correlation with team size is weak (r = -0.09), so team size is a minor factor in this dataset.

### 5. Delays drive cost overruns

Average cost overrun by project type (each `#` = 1%):

```
ERP     | ################ 16.5%
AI/ML   | ############### 15.4%
Cloud   | ########## 10.1%
Data    | ########## 9.7%
Mobile  | ###### 6.4%
Web     | ##### 5.2%
```

- Delayed projects average an 11.7% cost overrun, versus 3.6% for on-time projects.
- Delay days and cost overrun % have the strongest relationship in the data (r = 0.69).
- 114 of 250 projects exceeded their budget by more than 10%.

Top 5 cost overruns:

| Project | Type | Delay (days) | Cost Overrun % |
|---|---|---|---|
| P229 | AI/ML | 44 | 30.7 |
| P027 | ERP | 64 | 28.5 |
| P246 | ERP | 46 | 28.5 |
| P112 | ERP | 63 | 28.0 |
| P073 | ERP | 20 | 27.7 |

### 6. Overtime does not fix delays

| Overtime Level | Avg Delay (days) | Avg Cost Overrun % | Avg Task Completion % |
|---|---|---|---|
| Low | 7.3 | 7.8 | 95.6 |
| Medium | 11.6 | 9.1 | 95.5 |
| High | 11.4 | 11.8 | 95.8 |

High-overtime projects cost more, but task completion stays the same. Extra hours add cost without improving completion.

### 7. Delays hurt client satisfaction

| Group | Avg Client Satisfaction (out of 5) |
|---|---|
| On-time projects | 4.53 |
| Delayed projects | 3.95 |

### 8. Monthly performance varies

Average delay by month (each `#` = 1 day):

```
Jan | ############ 11.9
Feb | ################## 18.1
Mar | ######## 8.1
Apr | ###### 6.1
May | ############ 12.0
Jun | ######### 9.3
Jul | ############ 11.7
Aug | ######## 7.5
Sep | ############### 14.9
Oct | #### 4.1
Nov | ######### 9.5
Dec | ######## 8.4
```

Delay peaks in February and September and is lowest in October. Since the data is synthetic, these swings are mostly random; the analysis shows how a real trend would be tracked.

### Correlation with Delay Days

| Factor | Correlation |
|---|---|
| Cost overrun % | 0.69 |
| Client changes | 0.38 |
| Bugs found | 0.37 |
| Overtime hours | 0.11 |
| Team size | -0.09 |
| Client satisfaction | -0.41 |
| Task completion rate | -0.55 |

Correlation does not prove causation. These are associations found in the dataset.


## Dataset

`data/it_project_data.csv` has one row per project (250 rows, 17 columns, no missing values, no duplicates).

| Column | Description |
|---|---|
| Project_ID | Unique project identifier |
| Project_Type | Web / Mobile / Data / Cloud / AI/ML / ERP |
| Department | Development / Testing / Data / Infrastructure |
| Month | Month of the project |
| Team_Size | Number of team members |
| Planned_Duration_Days | Planned duration |
| Actual_Duration_Days | Actual duration |
| Tasks_Planned | Planned tasks |
| Tasks_Completed | Completed tasks |
| Bugs_Found | Bugs identified |
| Bugs_Fixed | Bugs fixed |
| Client_Changes | Client requirement changes |
| Planned_Budget | Original budget (Rs.) |
| Actual_Cost | Actual cost (Rs.) |
| Overtime_Hours | Extra working hours |
| Project_Status | Completed / Delayed / Ongoing |
| Client_Satisfaction | Rating from 1 to 5 |

`data/it_project_data_processed.csv` adds these calculated columns:

| Column | Formula |
|---|---|
| Delay_Days | Actual_Duration_Days - Planned_Duration_Days |
| Task_Completion_Rate | Tasks_Completed / Tasks_Planned * 100 |
| Bug_Resolution_Rate | Bugs_Fixed / Bugs_Found * 100 |
| Budget_Variance | Actual_Cost - Planned_Budget |
| Cost_Overrun_Pct | (Actual_Cost - Planned_Budget) / Planned_Budget * 100 |

---

## Project Structure

```text
ProManager/
├── images/
├── powerbi/
│   └── simple_dashboard_project_delay.pbix
├── src/
│   ├── analytics.py
│   └── chats.py
├── visualizations/
│   ├── average_delay_by_department.png
│   ├── bugs_vs_delay.png
│   ├── planned_vs_actual_days.png
│   ├── projects_by_delay_reason.png
│   └── projects_by_department.png
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How to Run

```bash
git clone https://github.com/Tanishq747Shivasharan/Variance.git
cd Variance
pip install -r requirements.txt
python src/analytics.py
```

## Team

* Kranti Ingale
* Ankita Salpekar
* Ankita Karke
* Ayush Bage
* Tanishq Shivasharan