import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Plot aesthetics
sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams.update({'figure.dpi': 130, 'axes.titlesize': 13,
                     'axes.labelsize': 11, 'figure.figsize': (7, 4)})
print('Libraries loaded ✓')

# ── 1 · Load Dataset ──────────────────────────────────────────────────────────
df = pd.read_csv('student-mat.csv')
print(f'\nShape: {df.shape}')
print(df.head())

# ── 2 · Explore & Clean Data ─────────────────────────────────────────────────

# 2a · Dataset Info
print('\n── Dataset Info ──')
df.info()

# 2b · Missing Values
missing = df.isnull().sum()
print('\nMissing values per column:')
print(missing[missing > 0] if missing.any() else 'No missing values found ✓')

# 2c · Duplicate Rows
dupes = df.duplicated().sum()
print(f'\nDuplicate rows: {dupes}')
if dupes > 0:
    df = df.drop_duplicates()
    print(f'Removed {dupes} duplicates. New shape: {df.shape}')
else:
    print('No duplicates found ✓')

# 2d · Summary Statistics
print('\n── Summary Statistics ──')
print(df.describe().round(2))

# ── 3 · Analysis Questions ───────────────────────────────────────────────────

# Q1 · Average Final Grade (G3)
print('\n── Q1: Average Final Grade (G3) ──')
avg_g3 = df['G3'].mean()
median_g3 = df['G3'].median()
print(f'Mean   G3: {avg_g3:.2f} / 20')
print(f'Median G3: {median_g3:.2f} / 20')

# Q2 · Students Scoring Above 15
print('\n── Q2: Students Scoring Above 15 ──')
above_15 = (df['G3'] > 15).sum()
pct = above_15 / len(df) * 100
print(f'Students scoring above 15: {above_15} ({pct:.1f}% of total)')

# Q3 · Study Time vs Performance (Correlation)
print('\n── Q3: Study Time vs Performance ──')
corr = df['studytime'].corr(df['G3'])
print(f'Pearson correlation (studytime vs G3): {corr:.4f}')

grp = df.groupby('studytime')['G3'].agg(['mean', 'count'])
grp.index = ['<2 hrs', '2–5 hrs', '5–10 hrs', '>10 hrs']
grp.columns = ['Avg G3', 'Count']
print('\nAverage G3 by Study Time:')
print(grp.round(2))

# Q4 · Gender Performance Comparison
print('\n── Q4: Gender Performance Comparison ──')
gender_stats = df.groupby('sex')['G3'].agg(['mean', 'median', 'count'])
gender_stats.columns = ['Mean G3', 'Median G3', 'Count']
gender_stats.index = ['Female', 'Male']
print(gender_stats.round(2))

winner = 'Female' if gender_stats.loc['Female', 'Mean G3'] > gender_stats.loc['Male', 'Mean G3'] else 'Male'
diff = abs(gender_stats['Mean G3'].diff().iloc[-1])
print(f'\n→ {winner} students score higher on average by {diff:.2f} points.')

# ── 4 · Visualizations ───────────────────────────────────────────────────────

# 4a · Distribution of Final Grades (G3)
fig, ax = plt.subplots()
ax.hist(df['G3'], bins=range(0, 22), color='steelblue', edgecolor='white', linewidth=0.7)
ax.axvline(df['G3'].mean(), color='crimson', linestyle='--', linewidth=1.5,
           label=f"Mean = {df['G3'].mean():.1f}")
ax.set_xlabel('Final Grade (G3)')
ax.set_ylabel('Number of Students')
ax.set_title('Distribution of Final Grades (G3)')
ax.legend()
ax.xaxis.set_major_locator(mticker.MultipleLocator(2))
plt.tight_layout()
plt.savefig('outputs/hist_grades.png', dpi=130)
plt.show()
print('Saved: outputs/hist_grades.png ✓')

# 4b · Study Time vs Final Grade (Scatter + Trend)
fig, ax = plt.subplots()
jitter = np.random.uniform(-0.15, 0.15, len(df))
ax.scatter(df['studytime'] + jitter, df['G3'], alpha=0.35, s=25, color='teal')

m, b = np.polyfit(df['studytime'], df['G3'], 1)
xs = np.linspace(1, 4, 100)
ax.plot(xs, m * xs + b, color='crimson', linewidth=2,
        label=f'Trend (r={df["studytime"].corr(df["G3"]):.2f})')

ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['<2 hrs', '2–5 hrs', '5–10 hrs', '>10 hrs'])
ax.set_xlabel('Weekly Study Time')
ax.set_ylabel('Final Grade (G3)')
ax.set_title('Study Time vs Final Grade')
ax.legend()
plt.tight_layout()
plt.savefig('outputs/scatter_study_grade.png', dpi=130)
plt.show()
print('Saved: outputs/scatter_study_grade.png ✓')

# 4c · Average Final Grade by Gender
gender_mean = df.groupby('sex')['G3'].mean().rename({'F': 'Female', 'M': 'Male'})
gender_sem  = df.groupby('sex')['G3'].sem().rename({'F': 'Female', 'M': 'Male'})

fig, ax = plt.subplots(figsize=(5, 4))
colors = ['#E07B8A', '#5B9BD5']
bars = ax.bar(gender_mean.index, gender_mean.values,
              yerr=gender_sem.values * 1.96,
              capsize=5, color=colors, edgecolor='white', linewidth=0.8)

for bar, val in zip(bars, gender_mean.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f'{val:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_ylim(0, 22)
ax.set_xlabel('Gender')
ax.set_ylabel('Average Final Grade (G3)')
ax.set_title('Average Final Grade by Gender (with 95% CI)')
plt.tight_layout()
plt.savefig('outputs/bar_gender_grade.png', dpi=130)
plt.show()
print('Saved: outputs/bar_gender_grade.png ✓')

print('\n✅ All analysis complete! Check the outputs/ folder for charts.')
