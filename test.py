def test(arg1, *args, **kwargs):
    print('arg1:', arg1)
    print('args:', args)
    print('kwargs:', kwargs)

if __name__ == '__main__':
    test(1, 'ar1', 'ar2', 'ar3', kw1='kw11', kw2='kw22')

