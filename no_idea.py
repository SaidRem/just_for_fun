# There is an array of  integers. There are also 2 disjoint sets, A
# and B, each containing m integers. You like all the integers in set A 
# and dislike all the integers in set B. Your initial happiness is 0.
# For each i integer in the array, if i in A, you add 1 to your happiness.
# If i in B, you add -1 to your happiness. Otherwise, your happiness does not
# change. Output your final happiness at the end.

def happy(n1, a, b):
    happyness = 0
    for i in n1:
        if i in a:
            happyness += 1
        if i in b:
            happyness -= 1
    return happyness



if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    n1 = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(happy(n1, a, b))