def make_pizza(size, *toppings):
    """
    make pizza
    """
    print("\nMaking a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("-" + topping)
