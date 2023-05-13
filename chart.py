import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

# Load data from Excel file
data = pd.read_excel('student_marks.xlsx')

# Extract student names and marks
marks = data['Marks'].tolist()
semester = data['Semester'].tolist()

# Create interpolation function
f = interp1d(semester, marks, kind='cubic')

# Create curve graph with smoothed line
xnew = np.linspace(min(semester), max(semester), num=1000, endpoint=True)
plt.plot(xnew, f(xnew), '-')
plt.title('Student Marks')
plt.xlabel('Semester')
plt.ylabel('Marks')

plt.plot(semester, marks, 'o', color='blue')

# Show graph
plt.show()
