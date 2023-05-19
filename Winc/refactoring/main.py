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

    def get_contracts(self):
        for need in self.needs:
            need.lower()
            if need == "electrician":
                needed_specialist = getattr(electrician, 'name')
                self.contracts.append(needed_specialist) 
            elif need == "painter":
                needed_specialist = getattr(painter, 'name')
                self.contracts.append(needed_specialist) 
            elif need == "plumber":
                needed_specialist = getattr(plumber, 'name')
                self.contracts.append(needed_specialist) 
        return [contractor for contractor in self.contracts]


class Specialist:
    def __init__(self, name):
        self.name = name
        # self.price = price

class Electrician(Specialist):
    def __init__(self, name):
        super().__init__(name)

class Painter(Specialist):
    def __init__(self, name):
        super().__init__(name)

class Plumber(Specialist):
    def __init__(self, name):
        super().__init__(name)

class ContractCreator(Homeowner, Specialist):
    pass


if __name__ == "__main__":
    # create homeowners:
    alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ['painter', 'plumber'])
    bert = Homeowner("Bert Bertson", "Bertslane 231", ['plumber'])
    candice = Homeowner("Candice Candicedottir", "Candicelane 312", ['electrician', 'painter'])

    # create specialists:
    electrician = Electrician("Alice Aliceville")
    painter = Painter("Bob Bobsville")
    plumber = Plumber("Craig Craigsville")
    
    # testing results by printing:
    print("Alfred's contracts:", alfred.get_contracts())
    print("Bert's contracts:", bert.get_contracts())
    print("Candice's contracts:", candice.get_contracts())
