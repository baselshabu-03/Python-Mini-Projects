def kaprekar_step(num):
    num_str = f"{num:04d}"
    desc = int("".join(sorted(num_str, reverse=True)))
    asc = int("".join(sorted(num_str)))
    return desc - asc

def is_valid(num):
    num_str = f"{num:04d}"
    # Check for exactly 4 digits and at least two unique digits
    return len(num_str) == 4 and len(set(num_str)) > 1

def kaprekar_routine():
    user_input = input("Enter a 4-digit number (not all digits the same): ")
    
    try:
        num = int(user_input)
        if not is_valid(num):
            print("❌ Invalid input. Must be a 4-digit number with at least two different digits (e.g., not 1111).")
            return
        
        steps = 0
        while num != 6174:
            num = kaprekar_step(num)
            steps += 1
            print(f"Step {steps}: {num:04d}")
        
        print(f"\n✅ Kaprekar's constant 6174 reached in {steps} steps.")
        
    except ValueError:
        print("❌ Please enter a valid numeric 4-digit input.")

# Run the program
kaprekar_routine()