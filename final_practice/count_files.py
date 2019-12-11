import os
def count_files(): 
    count = 0
    for t in os.walk('.'):
        count += len(t[2])
    return count

# if __name__ == "__main__":
    # print(count_files())
