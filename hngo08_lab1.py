import sys 

def main():
    filename = sys.argv[1]
    with open(filename) as f: 
        arr = [int(line.strip()) for line in f] 

    print(findSingleton(arr))

def findSingleton(arr): 
    i = 0
    while i < len(arr) - 1: #loop as long as there is a pair in the list 
        if arr[i] != arr[i +1]: 
            return arr[i]
        i += 2 #skip to after a pair
    return arr[-1] #the last element should be a singleton 

if __name__ == "__main__": 
    main()

