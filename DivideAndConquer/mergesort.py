def merge_sort(vetor, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(vetor, start, mid)
        merge_sort(vetor, mid + 1, end)
        merge(vetor, start, mid, end)

def merge(vetor, start, mid, end):
    left_len = mid - start + 1
    right_len = end - mid

    left_vetor = [0] * left_len
    right_vetor = [0] * right_len

    for i in range(left_len):
        left_vetor[i] = vetor[start + i]

    for j in range(right_len):
        right_vetor[j] = vetor[mid + 1 + j]

    idx_left = 0
    idx_right = 0
    k = start

    while idx_left < left_len and idx_right < right_len:
        if left_vetor[idx_left] < right_vetor[idx_right]:
            vetor[k] = left_vetor[idx_left]
            idx_left += 1
        else:
            vetor[k] = right_vetor[idx_right]
            idx_right += 1
        k += 1

    while idx_left < left_len:
        vetor[k] = left_vetor[idx_left]
        idx_left += 1
        k += 1

    while idx_right < right_len:
        vetor[k] = right_vetor[idx_right]
        idx_right += 1
        k += 1

vetor = [5, 2, 7, 6, 2, 1, 0, 3, 9, 4]
print(f'Vetor original: {vetor}')
merge_sort(vetor, 0, len(vetor) - 1)
print(f'Vetor ordenado: {vetor}')
