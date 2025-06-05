a , b = input().split()
def longer_string(a,b):
    if len(a) >= len(b):
        print(a)
    else:
        print(b)

longer_string(a,b)