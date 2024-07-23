import random
import time 

operators = [ "+" , "-" , "*" ]
min_operand = 1
max_operand = 10

total_operations = 1

def generate_operation():
    left_side = random.randint(min_operand, max_operand)
    right_side = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    exp = str(left_side) + " " + operator + " " + str(right_side)
    answer = eval(exp)
    return exp, answer

wrong = 0

strat_time = time.time()

for i in range(total_operations):
    exp, answer = generate_operation()
    while True:
        guess = input(f"Problem-{i +1} : " + exp + "=")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()
total_time = end_time - strat_time
print(f"You finished the operations in {total_time} seconds.")



