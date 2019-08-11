# Problem : Forming a Magic Square

magic_squares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

def formingMagicSquare(s: list) -> int:
    sum_totals = []
    for m in magic_squares:
        total = 0
        for m_row, s_row in zip(m, s):
            for i, j in zip(m_row, s_row):
                if i != j:
                    total += abs(i-j)
        sum_totals.append(total)
    return min(sum_totals)
