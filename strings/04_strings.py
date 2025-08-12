letter = "my name is {} my country is {}"
name = "Alok"
country = "india"
print(letter.format(name,country))
f_string = (f"my name is {name} my country is {country}")
print(f_string)
money = 23.3435643
handle_float_numbers = f"The money we have to taken is 2 decimal {money : .2f}"
print(handle_float_numbers)