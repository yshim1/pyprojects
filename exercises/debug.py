def mutate(A):
    B = []
    for item in A:
        new_item = item * 2
    B.append(new_item)
    print(B)
mutate([1,2,3,5,8,13])