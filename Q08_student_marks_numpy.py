import numpy as np

#student names
students = np.array(["S1", "S2", "S3", "S4", "S5"])

#mid-semester marks
mid_sem = np.array([
    [65,70,68,72],
    [78,75,80,77],
    [55,60,58,62],
    [82,85,80,88],
    [70,68,72,74]
])

#end-semester marks
end_sem = np.array([
    [72,78,75,80],
    [84,82,86,83],
    [65,68,66,70],
    [88,80,85,92],
    [78,75,80,82]
])

#total marks for each student in mid
mid_total = np.sum(mid_sem, axis=1)

#total marks for each student in end
end_total = np.sum(end_sem, axis=1)

end_average = np.mean(end_sem, axis=1)

percentage_improvement = ((end_total-mid_total)/mid_total)*100

#display results
print("Students MidTotal EndTotal EndAverage Improvement(%)")
print("-"*60)

for i in range(len(students)):
    print(f"{students[i]:<10} {mid_total[i]:<10} {end_total[i]:<10} {end_average[i]:<12.2f} {percentage_improvement[i]:.2f}")