from mathematics import factorial

nums: list[str] = input().split()

result: list[int] = []
for n in nums:
    fact: int = factorial(int(n))  # CTRL + Q
    result.append(fact)

print(result)

# 5 18 4 13
