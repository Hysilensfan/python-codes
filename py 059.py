# first method
def operating(expr: str) -> int:
    nums, ops, i, n = [], [], 0, len(expr)  # i stand for "index"
    while i < n:
        c = expr[i]
        if c == '-' and (i == 0 or expr[i - 1] in "+-*"):  # specific process to the '-' sign in the index 0
            j = i + 1
            num = "-"
            while j < n and expr[j].isdigit():
                num += expr[j]
                j += 1
            nums.append(int(num))
            i = j
        elif c.isdigit():
            num = ""
            while i < n and expr[i].isdigit():
                num += expr[i]
                i += 1
            nums.append(int(num))
        elif c in "+-*":
            ops.append(c)
            i += 1
        else:
            i += 1
    new_nums, new_ops = [nums[0]], []
    for i in range(len(ops)):
        if ops[i] == "*":
            new_nums[-1] *= nums[i + 1]
        else:
            new_nums.append(nums[i + 1])
            new_ops.append(ops[i])
    result = new_nums[0]
    for i in range(len(new_ops)):
        result = result + new_nums[i + 1] if new_ops[i] == "+" else result - new_nums[i + 1]

    return result


[print("TRUE" if all(a == c for a, c in [map(operating, input().split("=="))]) else "FALSE") for _ in range(4)]

# second method
[print("TRUE" if all(a == c for a, c in [map(eval, input().split("=="))]) else "FALSE") for _ in range(4)]

