def max_triangle_sum(tri):
    while len(tri) > 1:
        lower_row = tri.pop()
        upper_row = tri.pop()
        tri.append([max(lower_row[i], lower_row[i+1]) + t
                    for i, t in enumerate(upper_row)])
    return tri[0][0]

triangle = []
with open('p067_triangle.txt') as fp:
    split_triangle = [list(map(int, line.split())) for line in fp]


print(max_triangle_sum(split_triangle))