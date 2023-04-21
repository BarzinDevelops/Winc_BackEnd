# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part1: Greeting

def greet(name, greeting="Hello, <name>!"):
    if '<name>' in greeting:
        greeting = f"{greeting.replace('<name>', name)}"
    else:
        greeting = f"{greeting}, {name}!"  
    return greeting

print(greet('barry'))
print(greet('barry', 'salam'))



# Part2: Force

bodies = {
    'sun': 274,
    'jupiter': 24.9,
    'neptune': 11.2,
    'saturn': 10.4,
    'earth': 9.8,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.6,
    'pluto': 0.6,
}

def force(mass, body='earth'):
    return round(mass * bodies[body], 1)

print(force(2,'moon'))



