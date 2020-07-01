print("let's practice")
print('you\'d need to know escapes with \\ that do:')
print('\n newline and \t tabs.')

poem = """
\t lovely world
blah blah \n some more text
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")

five = 10 - 2 + 3 - 6
print(f"this should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates  # three output values

start_point = 10000
beans, jars, crates = secret_formula(start_point)  # notice it's named as beans and not jelly_beans

# another way to format strings
print("with a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"we'd have {beans} beans, {jars} jars and {crates} crates")

start_point = start_point / 10

print("we also do that this way")
formula = secret_formula(start_point)
# this is an easy way to apply a list ot a format string
print("we'd have {} beans, {} jars and {} crates.".format(*formula))


