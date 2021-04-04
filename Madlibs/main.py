# Jeremy Palad

# string concatenation
any_name = input("Enter a name: ")
silly_word = input("Enter a silly name: ")
num_years = input("Enter a number: ")
a_noun = input("Enter a noun: ")
first_adj = input("Enter first adjective: ")
sec_adj = input("Enter second adjective: ")
third_adj = input("Enter third adjective: ")
fourth_adj = input("Enter fourth adjective: ")
fifth_adj = input("Enter fifth adjective: ")
relative = input("Enter a relative's name: ")
first_verb = input("Enter a verb: ")
sec_verb = input("Enter another verb: ")


madlib = f"Hello, my name is austronaut {any_name}. I am on my way to planet {silly_word}. I will be gone for " \
         f"{num_years} days. I am very {first_adj} about the trip but I will miss my {a_noun}. " \
         f"I have heard that the atmosphere there is {sec_adj}. Luckily my {relative} packed me a jacket to keep me " \
         f"{third_adj}. When I land on the planet I will {first_verb} for joy. I am {fourth_adj} to {sec_verb} on " \
         f"another planet. I could not be more {fifth_adj} for this trip!"

print(madlib)
