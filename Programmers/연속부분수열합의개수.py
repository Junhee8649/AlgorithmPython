def solution(elements):
    L = len(elements)
    all_sum = sum(elements)
    sum_elements = set(elements)
    elements = elements + elements[:-2]

    for i in range(2, L):
        for j in range(L):
            sum_elements.add(sum(elements[j:j+i]))
    sum_elements.add(all_sum)

    return len(sum_elements)