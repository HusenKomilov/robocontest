def solve(year: int) -> str:
    a = ""
    if year <= 9:
        a += f"000"
    elif year <= 99:
        a += f"00"
    elif year <= 999:
        a += f"0"
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        txt = f"12/09/{a}{year}"
    else:
        txt = f"13/09/{a}{year}"
    return txt


year = int(input())
print(solve(year))
