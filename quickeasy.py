import time ,random

def quicksort(arr,low,high,randomized=False):
    if low <high :
        if randomized:
            pivot_indx=random.randint(low,high)
            print(f"Randomly selected pivot index: {pivot_indx}, value: {arr[pivot_indx]}")  # Add this line
            arr[pivot_indx] ,arr[high]=arr[high], arr[pivot_indx]
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1,randomized)
        quicksort(arr,pivot+1,high ,randomized)

def partition(arr,low,high):
    pivot, i=arr[high],low
    for j in range(low,high):
        if arr[j]<=pivot:
            arr[i],arr[j] = arr[j] , arr[i]
            i+=1
    arr[i],arr[high] =arr[high], arr[i]
    return i

def analyze_quicksort(arr):
    for variant in ['Deterministic', 'Randomized']:
        arr_copy=arr.copy()
        start_time=time.perf_counter()
        quicksort(arr_copy ,0, len(arr)-1 ,randomized=(variant=='Randomized'))
        exe_time=time.perf_counter()-start_time
        print(f"{variant} quicksort result:{arr_copy}")
        print(f"execution time :{exe_time:.6f} seconds")

if __name__=="__main__":
    arr=list(map(int ,input("enter elements").split()))
    print("og array:",arr)
    analyze_quicksort(arr)
    
