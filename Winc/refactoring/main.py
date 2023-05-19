__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name,
        self.address = address
        self.needs = needs
        self.contracts = []
    
    def add_needs(self, specialist_need):
        self.needs.extend(specialist_need)

    def get_contracts(self, specialists):
        for need in self.needs:
            need.lower()
            if need == "electrician":
                best_electrician = best_offer(specialists['electricians'])
                self.contracts.append(best_electrician) 
            elif need == "painter":
                best_painter = best_offer(specialists['painters'])
                self.contracts.append(best_painter) 
            elif need == "plumber":
                best_plumber = best_offer(specialists['plumbers'])
                self.contracts.append(best_plumber) 
        return [contractor for contractor in self.contracts]


class Specialist:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Electrician(Specialist):
    def __init__(self, name, price):
        super().__init__(name, price)
class Painter(Specialist):
    def __init__(self, name, price):
        super().__init__(name, price)
class Plumber(Specialist):
    def __init__(self, name, price):
        super().__init__(name, price)

def best_offer(needed_specialists):
    best_price = float(needed_specialists[0].price)
    chosen = {}
    for needed_specialist in needed_specialists:
        needed_specialist.price = float(needed_specialist.price)
        if needed_specialist.price < best_price:
            best_price = needed_specialist.price
            chosen = {'name': needed_specialist.name, 'price': needed_specialist.price}    
    return chosen['name']



if __name__ == "__main__":
    # create homeowners:
    alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ['painter', 'plumber'])
    bert = Homeowner("Bert Bertson", "Bertslane 231", ['plumber'])
    candice = Homeowner("Candice Candicedottir", "Candicelane 312", ['electrician', 'painter'])
    marta = Homeowner("Marta Legends", "Testlane 555", ['painter', 'plumber', 'electrician'])

    # create specialists:
    Alice = Electrician("Alice Aliceville", 35)
    Ahmed = Electrician("Ahmed Bassar", 18)
    Fatoush = Electrician("Fatoush Kashflow", 20)
    
    Bob = Painter("Bob Bobsville", 23)
    Kees = Painter("Kees Andermans", 19.50)
    Leo = Painter("Leo Vaardig", 21)
    
    Craig = Plumber("Craig Craigsville", 20)
    Henk = Plumber("Henk Beentjes", 16)
    Stephan = Plumber("Stephan Kamerman", 17.50)
    
    # available specialists dictionary:
    current_specialists = {
        "electricians": [Alice, Ahmed, Fatoush],
        "painters": [Bob, Kees, Leo],
        "plumbers": [Craig, Henk, Stephan]
    }
    
    # testing results by printing:
    print("Alfred's contracts:", alfred.get_contracts(current_specialists))
    print("Bert's contracts:", bert.get_contracts(current_specialists))
    print("Candice's contracts:", candice.get_contracts(current_specialists))
    print("Marta's contracts:", marta.get_contracts(current_specialists))

    
    
