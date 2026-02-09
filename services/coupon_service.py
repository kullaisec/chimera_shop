USED = set()

def apply_coupon(code, total):
    if code in USED:
        return total

    if code.startswith("SAVE"):
        discount = int(code.replace("SAVE", ""))
        USED.add(code)
        return max(total - discount, 0)

    return total
