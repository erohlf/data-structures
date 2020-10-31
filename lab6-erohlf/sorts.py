import random
import time

def selection_sort(list):
    count = 0
    for i in range(len(list)-1,0,-1):
        max = 0
        for j in range(1, i+1):
            if list[j] > list[max]:
                max = j
            count += 1

        temp = list[i]
        list[i] = list[max]
        list[max] = temp
    return count
    
def insertion_sort(list):
    count = 0
    for i in range(1,len(list)):
        current = list[i]
        pos = i

        while pos > 0 and list[pos-1] > current:
            list[pos] = list[pos-1]
            pos -= 1
            count += 1

        list[pos] = current
    return count

   

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 10000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

