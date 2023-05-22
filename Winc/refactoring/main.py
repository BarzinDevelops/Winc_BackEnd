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
            best = best_offer(specialists[need])
            self.contracts.append(best)
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
    return sorted(needed_specialists, key=lambda x: x.price)[0].name


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
        "electrician": [Alice, Ahmed, Fatoush],
        "painter": [Bob, Kees, Leo],
        "plumber": [Craig, Henk, Stephan]
    }
    
    # testing results by printing:
    print("Alfred's contracts:", alfred.get_contracts(current_specialists))
    print("Bert's contracts:", bert.get_contracts(current_specialists))
    print("Candice's contracts:", candice.get_contracts(current_specialists))
    print("Marta's contracts:", marta.get_contracts(current_specialists))

    
    
