# def product_all(*args):
    # p = 1
    # for item in args:
        # try:
            # p += p * (item-1)
        # except Exception as e:
            # pass

    # return p

def product_all(*args):
    p = 1
    for item in args:
        if isinstance(item, (int, float)):
            p *= item

    return p

if __name__ == "__main__":
    print(product_all()) 
    print(product_all('a', [ ], 12, 1.1, 'b')) 

