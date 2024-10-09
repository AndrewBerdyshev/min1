def bitsCount(n: int) -> int:
    count = 0
    if n < 0:
        count += 1
    while n != 0 and n != -1:
        count += n & 1
        n >>= 1
    return count
print(bitsCount(int(input())))