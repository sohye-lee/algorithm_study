[base, unit, price] = list(map(int, input().split()))

ct = 1

if price <= unit:
    print(-1)
else:
    print(int(base / (price-unit)) + 1)