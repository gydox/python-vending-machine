class VendingMachine:
    """
    A class representing a vending machine that sells drinks.

    Attributes:
        drinks (list): A list of dictionaries containing information about available drinks,
                    including name, price, and stock.
        balance (dict): A dictionary representing the vending machine's balance of notes
                        and their quantities.
        credit (dict): A dictionary representing the user's credit, with note denominations
                    as keys and the quantity of each denomination as values.
    """

    def __init__(self):
        self.drinks = [
            {"name": "Coca-cola", "price": 3, "stock": 1},
            {"name": "Sprite", "price": 45, "stock": 8},
            {"name": "100 Plus", "price": 5, "stock": 5},
            {"name": "Mermaid's Teardrop", "price": 106, "stock": 0},
        ]

        self.balance = {
            100: 1,
            50: 10,
            20: 10,
            10: 10,
            5: 30,
            1: 2
        }

        self.credit = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            1: 0
        }

    def display_drinks(self):
        print("========== DRINKS SELECTION ==========")
        for i, drink in enumerate(self.drinks):
            print(str(i) + " : " + drink['name'] + " RM" +
                  str(drink['price']) + " x" + str(drink['stock']))

        print("Total credits:", self.get_total_credit())
        print("======================================")

        for denomination, count in self.balance.items():
            print("RM" + str(denomination) + ": " + str(count))

    def get_total_credit(self):
        total = 0
        for key, value in self.credit.items():
            total += key * value
        return total

    def add_money(self, amount):
        print("amount",  amount)
        if amount not in self.balance:
            print("Invalid note")
            return 0
        else:
            self.credit[amount] += 1
            print("Successfully added " + str(amount) + " to credit")
            self.get_total_credit()
            return amount

    def return_credit(self):
        for key in self.credit:
            self.credit[key] = 0
        print("Returned all credit")

    def buy_drink(self, drink_index):
        if drink_index >= 0 and drink_index < len(self.drinks):
            selected_drink = self.drinks[drink_index]
            if self.drinks[drink_index]["stock"] > 0:
                print("Buying", selected_drink["name"],
                      "at RM"+str(selected_drink["price"]))
                price = selected_drink["price"]
                current_credit = self.get_total_credit()
                if current_credit < price:
                    print("Credit: RM" + str(current_credit) +
                          " .Insufficient credit, add more money")
                else:
                    change = self.get_change(current_credit - price)
                    if change != None:

                        # Deduct balance from change
                        print("Deducting vending machine balance")
                        for key in self.balance:
                            if key in change:
                                self.balance[key] -= change[key]
                        print("return change to user :")
                        for key, value in change.items():
                            print("RM"+str(key) + ": " + str(value), end=" ")

                        # Clear user credit
                        for key in self.credit:
                            self.credit[key] = 0

                        # Dispense drink
                        self.drinks[drink_index]["stock"] - 1
                        print("\nDispensing Drink: "+selected_drink["name"])
                        print("Transaction complete! Enjoy your drink.")

                    else:
                        print("Returning credit...")
                        self.return_credit()
            else:
                print(selected_drink["name"] + " not enough stock")
        else:
            print("invalid selection")

    def get_change(self, amount):
        change = {}
        while amount > 0:
            for key, value in self.balance.items():
                # print("Checking", key, "note(s)")
                if amount >= key and value > 0:
                    n_key = min(
                        amount//key, value)
                    change[key] = n_key
                    amount -= key * n_key
                    # print("Vending machine can deduct " + str(n_key) +
                    #       "x RM" + str(key) + " note(s)")
            if amount > 0:
                print("Vending machine has not enough change")
                return None
        return change


if __name__ == "__main__":
    vm = VendingMachine()
    while True:
        vm.display_drinks()
        print("1 - Add money")
        print("2 - Buy a drink")
        print("3 - Eject money")
        choice = input("Enter your selection (1-3 or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        elif int(choice) < 1 or int(choice) > 3:
            print("Invalid selection")
        else:
            if int(choice) == 1:
                denomination = input(
                    "Enter the note denomination you want to add: \n")
                vm.add_money(int(denomination))
            elif int(choice) == 2:
                drink_selection = input(
                    "Which drink would you like? (choose drink index) \n")
                vm.buy_drink(int(drink_selection))
            elif int(choice) == 3:
                print("user ejected money")
                vm.return_credit()
