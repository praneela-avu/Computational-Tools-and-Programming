import numpy as np

marks = [78,85,92,67,88,73,95,81,76,89]
temperature = [28.5,30.2,29.8,31.4,27.9,32.1,30.5]
sales = [12500,13800,14200,11900,15100,14750,16000]

data = {"Marks":marks, "Temperature":temperature, "Sales":sales}

for name,values in data.items():
    arr = np.array(values)

    print("\n",name)
    print("Mean=",np.mean(arr))
    print("Median=",np.median(arr))
    print("Standard Deviation =",np.std(arr))
    print("Minimum=",np.min(arr))
    print("Maximum=",np.max(arr))

    #without using NumPy

    mean = sum(values)/len(values)

    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 == 0:
        median = (sorted_values[n//2-1] + sorted_values[n//2])/2
    else:
        median = sorted_values[n//2]

    variance = sum((x-mean)**2 for x in values)/len(values)
    standard_deviation = variance**0.5

    print("\nWithout NumPy")
    print("Mean=",mean)
    print("Median=",median)
    print("Standard Deviation =",standard_deviation)
    print("Minimum=",min(values))
    print("Maximum=",max(values))