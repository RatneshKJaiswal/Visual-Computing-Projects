letter = "Hey my name is {} and I am from {}"
country="India"
name="Ratnesh"

print(letter.format(name,country))

# to have variables in string
print(f"Hey my name is {name} and I am from {country}")


txt = "For only {price:.2f} .2 decimal places"
print(txt.format(price=64.4653))

price=64.2465
txt = f"For only {price:.2f} .2 decimal places"
print(txt)


# when curly bracket is needed
txt = f"Hey my name is {{name}} and I am from {{country}}"
print(txt)