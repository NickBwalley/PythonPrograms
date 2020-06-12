#function to sort an array using bubbleSort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [466,979,549,898,344,561,663,199,79];
z = len(arr)
print("The Array Before Sorting is: ")
for i in range(z):
    print(arr[i])
print("The Array After Sorting is: ")
bubbleSort(arr)
for j in range(z):
    print(arr[j])