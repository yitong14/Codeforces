# 04-递归排序算法
# 把一个list分成两部分，分别排序后合并

def sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    left_arr = sort(arr[:length//2])
    right_arr = sort(arr[length//2:])
    left_len = len(left_arr)
    right_len = len(right_arr)
    i = 0
    j = 0
    new_arr = []
    while i < left_len or j < right_len:
        if i >= left_len:
            new_arr += right_arr[j:]
            j = right_len
        elif j >= right_len:
            new_arr += left_arr[i:]
            i = left_len
        else:
            if left_arr[i] <= right_arr[j]:
                new_arr.append(left_arr[i])
                i += 1
            else:
                new_arr.append(right_arr[j])
                j += 1
    return new_arr


a_list = eval(input())
print(sort(a_list))
