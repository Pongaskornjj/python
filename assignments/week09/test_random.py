import random

def test_random():
    # สุ่มเลข 1-10 เก็บไว้ใน random_number
    random_number = random.randint(1, 100)
    
    # รับค่าจากผู้ใช้ เก็บใน guess_number
    guess_number = input("What is your guess number?: ")
    
    
    if random_number == guess_number:
        print("Congratulations")
        
    elif random_number < guess_number:
        print("too much")
        
    elif random_number > guess_number:
        print("too low")
        
    print(random_number)
 
test_random()