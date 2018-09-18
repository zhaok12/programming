n = int(raw_input().strip())
a = map(int, raw_input().strip().split())
m = int(raw_input().strip())
q = map(int, raw_input().strip().split())

for i in range(1, n):
    a[i] += a[i - 1]
idx = sorted(range(len(q)), key=lambda k: q[k])
result = q
start = 0
for i in range(n):
    j = 0
    for j in range(start, m):
        if q[idx[j]] <= a[i]:
            result[idx[j]] = i + 1
        else:
            start = j
            break
    if j >= m - 1:
        break
for item in result:
    print item
