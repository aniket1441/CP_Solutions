n = int(input())

# Check if it is possible to split by checking if the summation to n is even
s = (n * (n + 1)) // 2

if s % 2 == 0:
    subset_sum = s // 2
    # Possible
    a = set()
    b = set()
    for i in range(n, 0, -1):
        if i <= subset_sum:
            subset_sum -= i
            a.add(i)
        else:
            b.add(i)

    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)

else:
    print("NO")
