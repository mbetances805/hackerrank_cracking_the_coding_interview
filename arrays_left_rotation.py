def array_left_rotation(a, n, k):
    sub_set = [num for indx, num in enumerate(a) if indx < k]
    new_list = [num for indx, num in enumerate(a) if indx >= k] + sub_set
    
    print(' '.join(str(element) for element in new_list))
    
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')