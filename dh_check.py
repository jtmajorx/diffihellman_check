# I always forget how DH works so I wrote this
# little bit of code to remember.
import random
print("First, both Bob and Alice agree publically on a prime modulos and")
print("a generator.")
prime = input("[Optional] Enter a custom prime, leave black for default: ")
generator = input("[Optional] Enter a custom generator number, leave black for default: ")

if len(prime) == 0:
    p = 48112959837082048697
else:
    p = int(prime)
if len(generator) == 0:
    g = random.randint(1000000000,9999999999)
else:
    g = int(generator)

print(f"Your prime number is {p}, and the generator is {g}.\n\n")

## Alice start keygen
print("Starting with Alice, we'll select a private number then use")
print("that private number to generate a public number to share")
print("with Bob.")
alice_priv = int(input("Select a random private number for Alice: "))
alice_public = pow(g,alice_priv) % p
print(f"Raising {g} to the power of {alice_priv} mod{p} gives us Alice's public number, {alice_public}.\n\n")

## Bob start keygen
print("Now Bob runs a similar operation, using his own randomly generated")
print("private number.")
bob_priv = int(input("Select a random private number for Bob: "))
bob_public = pow(g,bob_priv) % p
print(f"Raising {g} to the power of {bob_priv} mod{p} gives us Bob's public number, {bob_public}.\n\n")

## Now the magic happens
print("Now we can test Diffie-hellman. If this was successful, ")
print("when Alice raises Bob's public number to the power of her")
print(f"own private number mod{p}, the result should be the same as when")
print(f"Bob raises Alice's public number to his own private number mod{p}.\n\n")
bob_shared = pow(alice_public,bob_priv) % p
alice_shared = pow(bob_public,alice_priv) % p
print(f"Checking... Alice believes the shared secret is {alice_shared}")
print(f"Checking... Bob believes the shared secret is {bob_shared}")
#
if (alice_shared == bob_shared):
    print("The shared secrets match!")
else:
    print("Something went wrong, shared secrets do not match.")
