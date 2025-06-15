from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt

# Data
students = [
    ("Alice", [88, 92, 85], 265),
    ("Bob", [78, 81, 79], 238),
    ("Charlie", [90, 87, 93], 270),
    ("David", [85, 90, 80], 255),
    ("Eva", [92, 95, 94], 281),
    ("Frank", [70, 75, 78], 223),
    ("Grace", [88, 82, 90], 260),
    ("Hannah", [93, 89, 91], 273),
    ("Ian", [76, 83, 79], 238),
    ("Jasmine", [89, 91, 92], 272),
    ("Kevin", [60, 65, 70], 195),
    ("Lily", [94, 90, 88], 272),
    ("Mason", [72, 78, 74], 224),
    ("Nina", [85, 88, 82], 255),
    ("Oscar", [91, 93, 90], 274),
]

subjects = ["Math", "Science", "English"]

# Calculations
num_students = len(students)
total_scores = {subject: 0 for subject in subjects}
for student in students:
    scores = student[1]
    for i, subject in enumerate(subjects):
        total_scores[subject] += scores[i]
averages = {subject: round(total_scores[subject] / num_students, 2) for subject in subjects}
top_scorer = max(students, key=lambda x: x[2])
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
rank_dict = {s[0]: i + 1 for i, s in enumerate(sorted_students)}

# Line Chart with Legend
plt.figure(figsize=(10, 6))
for student in students:
    plt.plot(subjects, student[1], marker='o', label=student[0])
plt.title('Student Marks by Subject')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.5)

# Added legend on the right outside plot area
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small', title="Students")

plt.tight_layout()
plt.savefig("line_chart.png", bbox_inches='tight')
plt.close()

# PDF
pdf = FPDF()

# Page 1 – Title Page
pdf.add_page()
pdf.set_fill_color(220, 245, 220)
pdf.rect(10, 10, 190, 277, 'DF')
pdf.set_text_color(33, 37, 41)
pdf.set_font("Arial", 'B', 36)
pdf.set_y(70)
pdf.cell(0, 20, "Greenwood High School", ln=True, align='C')
pdf.set_font("Times", 'BI', 24)
pdf.set_text_color(0, 128, 0)
pdf.cell(0, 15, "Annual Student Performance Report", ln=True, align='C')
pdf.set_font("Arial", 'I', 14)
pdf.set_text_color(100)
pdf.cell(0, 12, "\"Empowering Students for a Brighter Future\"", ln=True, align='C')
pdf.set_font("Arial", 'I', 16)
pdf.set_text_color(50)
pdf.cell(0, 15, "Academic Year: 2024 - 2025", ln=True, align='C')
pdf.ln(20)
pdf.set_font("Arial", '', 14)
pdf.set_text_color(80)
pdf.cell(0, 12, f"Report generated on {datetime.now().strftime('%d %B %Y')}", ln=True, align='C')

# Page 2 – Summary & Table
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_fill_color(173, 216, 230)
pdf.rect(10, 10, 190, 18, 'F')
pdf.set_y(12)
pdf.set_font("Helvetica", 'B', 16)
pdf.set_text_color(0, 70, 140)
pdf.cell(0, 10, "Student Performance Summary", ln=True, align='C')
pdf.set_fill_color(200, 230, 255)
pdf.rect(10, 28, 190, 3, 'F')
pdf.set_y(35)
pdf.set_text_color(0)

summary_points = [
    ("- Total Students:", str(num_students)),
    ("- Top Scorer:", f"{top_scorer[0]} (Total Marks: {top_scorer[2]})"),
]
for label, value in summary_points:
    pdf.set_x(12)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 8, label, ln=0)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, value, ln=1)

pdf.set_x(12)
pdf.set_font("Arial", 'B', 12)
pdf.cell(50, 8, "- Average Scores:", ln=1)
pdf.set_font("Arial", '', 12)
for subject in subjects:
    pdf.set_x(20)
    pdf.cell(0, 8, f"- {subject}: {averages[subject]}", ln=True)

pdf.ln(6)
pdf.set_font("Arial", 'B', 12)
pdf.set_fill_color(220, 220, 220)
pdf.cell(10, 10, "#", 1, 0, 'C', True)
pdf.cell(40, 10, "Name", 1, 0, 'C', True)
for subject in subjects:
    pdf.cell(30, 10, subject, 1, 0, 'C', True)
pdf.cell(25, 10, "Total", 1, 0, 'C', True)
pdf.cell(20, 10, "Rank", 1, 1, 'C', True)

pdf.set_font("Arial", '', 12)
for i, student in enumerate(students):
    name, scores, total = student
    rank = rank_dict[name]
    fill_color = (245, 245, 245) if i % 2 == 0 else (255, 255, 255)
    pdf.set_fill_color(*fill_color)
    pdf.cell(10, 10, str(i + 1), 1, 0, 'C', True)
    pdf.cell(40, 10, name, 1, 0, 'L', True)
    for score in scores:
        pdf.cell(30, 10, str(score), 1, 0, 'C', True)
    pdf.cell(25, 10, str(total), 1, 0, 'C', True)
    pdf.cell(20, 10, str(rank), 1, 1, 'C', True)

# Page 3 – Line Chart + Average Table + Report Summary
pdf.add_page()
pdf.set_fill_color(220, 245, 220)
pdf.rect(10, 10, 190, 25, 'F')
pdf.set_font("Helvetica", 'BI', 16)
pdf.set_text_color(0, 100, 0)
pdf.cell(0, 15, "Subject-wise Student Marks Overview", ln=True, align='C')
pdf.set_font("Helvetica", 'I', 12)
pdf.set_text_color(33, 37, 41)
pdf.cell(0, 10, "Each student's marks across all subjects", ln=True, align='C')

# Chart
pdf.image("line_chart.png", x=10, y=40, w=190)

# Moved average table a bit lower
pdf.set_y(155)
pdf.set_font("Arial", 'B', 12)
pdf.set_fill_color(200, 230, 255)
pdf.cell(95, 10, "Subject", 1, 0, 'C', True)
pdf.cell(95, 10, "Average Score", 1, 1, 'C', True)
pdf.set_font("Arial", '', 12)
pdf.set_fill_color(255, 255, 255)
for subject in subjects:
    pdf.cell(95, 10, subject, 1, 0, 'C', True)
    pdf.cell(95, 10, str(averages[subject]), 1, 1, 'C', True)

# Report Summary
pdf.set_y(220)
pdf.set_font("Arial", 'I', 11)
pdf.set_text_color(80)
pdf.multi_cell(
    0, 8,
    f"Report Summary:\n"
    f"- Greenwood High School analyzed {num_students} students across {len(subjects)} core subjects.\n"
    f"- The overall top scorer is {top_scorer[0]} with {top_scorer[2]} total marks.\n"
    f"- This report is generated using Python (FPDF + Matplotlib) for academic insights and visualization."
)

# Output
pdf.output("student_report.pdf")
print("✅ Final updated PDF generated: student_report_final_updated.pdf")
