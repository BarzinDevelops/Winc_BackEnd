# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
#1
leek_price = 2
#2
print(f"Leek is {str(leek_price)} euro per kilo.")

# ----------------------------------------------------- #
# Part 2
#1
order = 'leek 4'
#2
num =  order[order.find('4')]
#3
num= int(num)
#4
sum_total = num * leek_price
print(sum_total)

# ----------------------------------------------------- #
# Part 3
#1
broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'

#2
get_weight = broccoli_order[broccoli_order.find('1.6'):]
total_price = round(float(get_weight) * broccoli_price, 2)

#3: Use the +-operator to assemble and print a string that looks like 
# the following: '1.6kg broccoli costs 3.74e'
get_broccoli = broccoli_order[:broccoli_order.find(' ')]
print(f"{get_weight}kg {get_broccoli} costs {total_price}e")

