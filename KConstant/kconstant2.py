def kaprekar_step(num):
    num_str = f"{num:04d}"
    desc = int("".join(sorted(num_str, reverse=True)))
    asc = int("".join(sorted(num_str)))
    return desc - asc

def is_valid(num):
    num_str = f"{num:04d}"
    return len(num_str) == 4 and len(set(num_str)) > 1

def kaprekar_routine():
    print("=== Kaprekar's Constant Finder ===")
    print("Enter a 4-digit number (not all digits the same). Type 'exit' or 'quit' to end.\n")
    
    while True:
        user_input = input("Enter number: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Exiting the program. Goodbye, Avogadro!")
            break
        
        if not user_input.isdigit() or len(user_input) != 4:
            print("❌ Invalid input. Please enter exactly 4 digits.")
            continue
        
        num = int(user_input)
        if not is_valid(num):
            print("❌ Invalid number. All digits should not be the same.")
            continue
        
        steps = 0
        print("🔁 Starting Kaprekar routine...")
        while num != 6174:
            num = kaprekar_step(num)
            steps += 1
            print(f"Step {steps}: {num:04d}")
        
        print(f"✅ Kaprekar's constant 6174 reached in {steps} steps.\n")

# Run the program
kaprekar_routine()