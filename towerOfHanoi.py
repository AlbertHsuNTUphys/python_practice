def hanoi_tower(n ,i ,r ,f): 
    if n > 0:
        hanoi_tower(n-1, i, f, r)
        print(f'Move ring {n} from {i} to {f}') 
        hanoi_tower(n-1, r, i, f)
    return

# if __name__ == "__main__":
    # hanoi_tower(10, 'A', 'B', 'C')
