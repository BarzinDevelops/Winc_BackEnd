# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part1:

def greet(name, greeting="Hello, <name>!"):
    if '<name>' in greeting:
        greeting = f"{greeting.replace('<name>', name)}"
    else:
        greeting = f"{greeting}, {name}!"  
    return greeting

print(greet('barry'))
print(greet('barry', 'salam'))