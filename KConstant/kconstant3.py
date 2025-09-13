def kaprekar_step(num):
    """
    Given an integer 0..9999, return (desc_str, asc_str, result_int)
    where desc_str and asc_str are 4-char strings (with leading zeros when needed).
    """
    s = f"{num:04d}"
    desc_str = "".join(sorted(s, reverse=True))
    asc_str = "".join(sorted(s))
    desc = int(desc_str)
    asc = int(asc_str)
    result = desc - asc
    return desc_str, asc_str, result

def is_valid_input(s):
    """
    Accept 1 to 4 digit numeric strings. After zero-padding to 4 digits,
    reject if all digits are the same (e.g., '1111', '0000').
    """
    if not s.isdigit() or not (1 <= len(s) <= 4):
        return False, "Enter 1 to 4 digits (e.g., 3524 or 378 for 0378)."
    padded = s.zfill(4)
    if len(set(padded)) == 1:
        return False, "Invalid: all digits are the same after padding (e.g., 1111 or 0000)."
    return True, ""

def kaprekar_loop():
    print("=== Kaprekar's Constant — step-by-step ===")
    print("Enter 1–4 digits (they'll be treated as a 4-digit number with leading zeros).")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user = input("Enter number: ").strip()
        if user.lower() in ("exit", "quit"):
            print("👋 Exiting. Goodbye, Baselious!")
            break

        valid, msg = is_valid_input(user)
        if not valid:
            print("❌", msg)
            continue

        num = int(user.zfill(4))
        if num == 6174:
            print("🔔 You've entered 6174 — it's already Kaprekar's constant.\n")
            continue

        print("🔁 Performing Kaprekar routine (showing desc - asc = result):")
        steps = 0
        # Safety cap (Kaprekar reaches 6174 in at most 7 steps for valid 4-digit numbers,
        # but we cap at 20 to be extra-safe).
        while num != 6174 and steps < 20:
            desc_str, asc_str, num = kaprekar_step(num)
            steps += 1
            print(f"Step {steps}: {desc_str} - {asc_str} = {num:04d}")

        if num == 6174:
            print(f"✅ Reached 6174 in {steps} step{'s' if steps != 1 else ''}.\n")
        else:
            print("⚠️ Stopped after too many iterations (something unexpected happened).\n")

if __name__ == "__main__":
    kaprekar_loop()