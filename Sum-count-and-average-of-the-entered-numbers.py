total = 0.0
count  = 0

while True:
    input_user = input("Enter a number: ")
    if input_user.lower() == 'done':
        
        break
    try:
        input_user = float(input_user)
        total += input_user
        count  = count  + 1
        
    except ValueError:
        print("Error: Please enter numbers only!")


print(f"the Total is {total}.", f"the len is {count }", f"the averge is {total/count }")