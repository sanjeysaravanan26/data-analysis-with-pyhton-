 Student Performance Analysis

Project Overview

This project analyzes the academic performance of students using the **UCI Student Performance Dataset**. The analysis explores how study habits and gender relate to students' final grades (G3) through data cleaning, statistical analysis, and visualizations.

This project was completed as **Task 1** during my **Data Analytics Internship at Maincraft Technologies**.

---

 Objectives

- Load and explore the student performance dataset.
- Perform data cleaning and preprocessing.
- Analyze the distribution of final grades (G3).
- Study the relationship between weekly study time and final grades.
- Compare academic performance based on gender.
- Generate insightful visualizations for better understanding.

---

 Dataset

Dataset: `student-mat.csv`

The dataset contains information about students' demographics, study habits, and academic performance collected from a Portuguese secondary school.

---

 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

 Features

-  Load and preprocess the dataset
-  Check for missing values
-  Remove duplicate records
-  Calculate average final grade (G3)
-  Count students scoring above 15
-  Analyze correlation between study time and performance
-  Compare average grades by gender
-  Generate professional charts and visualizations

---

 Visualizations

The project generates the following visualizations:

- Distribution of Final Grades
- Study Time vs Final Grade
- Average Final Grade by Gender

All generated charts are automatically saved in the **outputs/** folder.

---

 Project Structure

student_performance_project/
│
├── student_performance_analysis.py
├── student-mat.csv
├── requirements.txt
├── README.md
└── outputs/
```

---

 Installation

Clone the repository

```bash
git clone https://github.com/your-username/student-performance-analysis.git
```

Move into the project folder

```bash
cd student-performance-analysis
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the project

```bash
python student_performance_analysis.py
```

---

 Key Insights

- Average Final Grade: **9.8 / 20**
- Weak positive correlation (**r ≈ 0.11**) between study time and final grade.
- Students who study more tend to score slightly better.
- Female students achieved a slightly higher average final grade than male students.
- Most students scored between **8 and 14 marks**.

---

 Dashboard

After running the project, the generated dashboard looks like this.

> Add your dashboard image to the repository (for example, `dashboard.png`) and display it using:

markdown
![Student Performance Dashboard](dashboard.png)


 Internship Details

Organization: Maincraft Technologies

Internship Domain: Data Analytics

Task: Student Performance Analysis using Python

---

