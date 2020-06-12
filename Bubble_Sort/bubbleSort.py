def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [949,232,676,590,844,331,991];
#print out the array before being sorted
print("The Array Elements before sorting: ")
for i in range (len(arr)):
    print(arr[i])
#sorting the Array
bubbleSort(arr);
#print out the Array elements after being sorted
print("The Array after being sorted is: ")
for j in range(len(arr)):
    print(arr[j])