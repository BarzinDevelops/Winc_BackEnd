# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# 1: The language spoken the most in Switzerland is the same as in Spain.
spain_language_most_spoken = "Castilian Spanish"
switzerland_language_most_spoken = "German"
print(spain_language_most_spoken == switzerland_language_most_spoken)

# 2: The most prevalent religion in Switzerland is the same as in Spain.
spain_prevalent_religion = "Roman Catholic"
switzerland_prevalent_religion = "Roman Catholic"
print(spain_prevalent_religion == switzerland_prevalent_religion)

# 3: The name length of Spain's capital does not equal that of Switzerland.
spain_capital = "Madrid"
switzerland_capital = "Bern"
print(len(spain_capital) != len(switzerland_capital))

# 4: Switzerland's GDP is greater than Spain's GDP.
spain_GDP =  37900
switzerland_GDP = 71000
print(spain_GDP > switzerland_GDP)

# 5: The population growth is less than 1% in Switzerland and Spain.
spain_population_growth =  0.12
switzerland_population_growth = 0.64
print(spain_population_growth < 1 and switzerland_population_growth < 1)

# 6: At least one of the two countries has a population count of over 10 million.
spain_population_count =  47222613
switzerland_population_count = 8563760
print(spain_population_count > 10000000 or switzerland_population_count > 10000000)

# 7: Exactly one of the two countries has a population count of over 10 million.
spain_population_count =  47222613
switzerland_population_count = 8563760
print((spain_population_count > 10000000) ^ (switzerland_population_count > 10000000))