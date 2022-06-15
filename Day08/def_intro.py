def greet():
    print("Hello")
    print("How do you do?")
    print("Hello World!")

# greet()

def greet_with_name(person):
    print(f"Hello {person}")
    print(f"How do you do {person}?")
    print("Hello World!")

# greet_with_name("Ahmed")
# greet_with_name("Maheen")

def greet_with(name, loc):
    print(f"hello {name}.")
    print(f"how is the weather in {loc}.")


greet_with(loc="Karachi", name="Ahmed")