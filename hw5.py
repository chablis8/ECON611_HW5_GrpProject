








# use recursion to find factorial
def find_factori(x):
    try:
        if x == 1 :
            return 1
        elif x<1 or not  (isinstance(x, int)):
            return 'no flaot & negatives'
        else:
            return x*find_factori(x-1)
    except Exception:
        return ('invalid input')

# test function
print(find_factori(-1))
