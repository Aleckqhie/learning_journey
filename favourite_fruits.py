def favorite_fruits():
    fruits = []
    print("Enter your favorite fruits one by one. Type 'done' when you are finished:")
    while True:
        fruit = input("Fruit: ")
        if fruit.lower() == 'done':
            break
        fruits.append(fruit)
    
    print("\nYour favorite fruits are:")
    for fruit in fruits:
        print(f"- {fruit}") 
favorite_fruits()
