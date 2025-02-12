def mergeSort(arr :list):
    # check if array is already sorted; a single element
    if len(arr) > 1:
        # find the middle of the array
        mid = len(arr)//2

        # divide the array into two halves of left and right
        left = arr[:mid]
        right = arr[mid:]

        #mergesort the left and right halves, respectively
        mergeSort(left)
        mergeSort(right)


        i = j = k = 0

        # copy data from temporary arrays left[] and right[]
        # for merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        # copy any remaining data
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1