# pの値がqの順番になり、それを出力する。
def inverse_permutation(size, perm):
    # 固定長
    q = [i+1 for i in range(size)]
    # pi = i が成り立つならそのまま出力
    if perm != q:
        for j in range(size):
            tmp = perm[j]
            q[tmp-1] = j + 1
            
    return ' '.join(map(str, q))

n = int(input())
p = list(map(int, input().split()))
print(inverse_permutation(n, p))
