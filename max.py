# Returns maximum repeating element in arr[0..n-1].
# The array elements are in range from 0 to k-1
def maxRepeating(arr, n):
    # Iterate though input array, for every element
    # arr[i], increment arr[arr[i]%k] by k
    k=100
    arr2=[0]*k
    for i in range(0, n):
        arr2[arr[i]] += 1

    # Find index of the maximum repeating element
    max = arr2[0]
    result = 0
    for i in range(1, k):

        if arr2[i] > max:
            max = arr2[i]
            result = i

    # Uncomment this code to get the original array back
    # for i in range(0, n):
    #    arr[i] = arr[i]%k

    # Return index of the maximum element
    return result