# python-vending-machine
## Python Vending Machine

A simple vending machine logic that will dispense the least amount of notes as change to the user. It has a main logic to make the code easier to test

## Features
- Display available drinks with prices and stock.
- Select a drink by index.
- Insert money into the machine.
- Vend a drink and return change.
- Automatically returns money if the selected drink is out of stock or the user does not have enough money.

## Prerequisites
Python > 3.6 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/gydox/python-vending-machine.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-vending-machine
    ```

3. Run the vending machine script:

    ```bash
    python vending_machine.py
    ```

## Usage interactions

The usage of the vending machine follows a traditional vending machine functionalities where user needs to insert enough money before pressing a button to dispense a drink.

1. **Add money**: Insert notes (one by one) to add money to your user credit balance.
2. **Buy a drink**: Select a drink and then choose to buy it. 
3. **Eject money**: At any point, you can choose to eject all the money in your user credit balance. 
