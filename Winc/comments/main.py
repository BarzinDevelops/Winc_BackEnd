# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
#######################################################################

# setting up a list with ages:
ages = [34, 20, 13, 44, 55, 32, 26, 48, 66] 

"""
--------------------------------------------------------------------
    Calculating the average of all ages in the ages list.
    First calculate the sum of all ages list items.
    Second count the total items in the list ages.
    Then devide the total amount of all ages by the count of items.
--------------------------------------------------------------------
"""
sum_ages = sum(ages)  # getting the sum of all ages in ages list
length_ages = len(ages) # getting the length of all items in ages list

"""
--------------------------------------------------------------------
    Then last step is to calculate the average by
    deviding the total amount of all ages by the count of items.
--------------------------------------------------------------------
"""
avg_age = sum_ages / length_ages

# printing the calculated average age:
print(" The average ages of the collection is:", int(avg_age))