def bitsCount(n: int) -> int:
    count = 0
    if n < 0:
        count += 1
    while n != 0 and n != -1:
        count += n & 1
        n >>= 1
    return count

def check(arg: int, res: int) -> bool:
    temp = bitsCount(arg)
    if temp != res:
        print(f"Function failed:\nArgument: {arg}\nExpected result: {res}\nActual result: {temp}\n")
        return False
    return True

if check(10, 2) + check(-123, 3) == 2:
    print("All tests passed!\n")