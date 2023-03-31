from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(num_facts):
    count = 0
    unique_facts = []
    while len(unique_facts) < num_facts:
        fact = random_koala_fact()
        if fact not in unique_facts:
            unique_facts.append(fact)
        if count > 1000:
            break
        count += 1
    return unique_facts
        

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    # print(random_koala_fact())
    print(unique_koala_facts(23))

