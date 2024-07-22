def Enter():

    person = input("Enter name:")
    coins = input("Enter coin number:")
    print(f"\n{person} has {coins} coins left.")
    #another way to write a string
    message = "\n%s has %s coins left." % (person, coins)
    message1 = "\n{} has {} coins left" .format(person, coins)
    message2 = "\n{1} has {0} coins left." .format(coins, person)
    print(message)
    print(message1)
    print(message2)

Enter()




