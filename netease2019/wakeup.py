
n, k = map(int, raw_input().strip().split())
A = map(int, raw_input().strip().split())
T = map(int, raw_input().strip().split())
max_invert = sum([(1-T[i])*A[i] for i in range(k)])
invert = max_invert
for i in range(1, n-k+1):
    invert = (1 - T[i + k - 1]) * A[i + k - 1] - (1 - T[i - 1]) * A[i - 1] + invert
    max_invert = max(invert, max_invert)
print sum([T[i]*A[i] for i in range(n)]) + max_invert
