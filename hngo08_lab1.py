import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python")
        return

    filename = sys.argv[1]
    with open(filename) as f:
        arr = [int(line.strip()) for line in f]

    print(findSingleton(arr))

def findSingleton(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if mid % 2 == 1:
               mid -= 1
        if arr[mid] == arr[mid + 1]: #the singleton is on the right side
               lo = mid + 2
        else: #the singleton is on the left side
               hi = mid

    return arr[lo]

if __name__ == "__main__":
    main()
