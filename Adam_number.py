def adamnumber(n):
    square=n**2
    reverse=int(str(n)[::-1])
    reverse_square=reverse**2
    reverse_square_reverse=int(str(reverse_square)[::-1])
    return square == reverse_square_reverse
    
n=int(input())
if adamnumber(n):
    print("True")
else:
    print("False")