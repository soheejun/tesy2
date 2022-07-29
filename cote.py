def solution(vals, x, m):
    max_xor = 0 
    v_max_xor = 0 

    for v in vals: 
        xor = v ^ x
        if max_xor < xor and v < m: 
            max_xor = xor 
            v_max_xor = v
    return v_max_xor  





if __name__ == '__main__': 
    n_test = int(input())
    from math import gcd
    for _ in range(n_test):
        n, x, y = map(int, input().split())
        x_y_gcd = x*y // gcd(x, y)
        count = 0 
        
    print("something wrong")
