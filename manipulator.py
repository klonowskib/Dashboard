class manipulator:
    def __init__(self):
        self.total_kwh = 0
        self.time = 0
        self.price_per_kwh = 0
        self.money_saved = 0

    # Method to get updates from the database after a given time period
    def update_total(self):
        print('Current: '.format(self.total_kwh))  # remove print
        self.total_kwh = self.total_kwh + 0  # get the new information from the database to add
        # push the new value for total energy produced to the front end
        print('Updated: '.format(self.total_kwh))  # remove print

    # Allows the price of energy to be updated by the admin
    def update_price(self, new_price):
        self.price_per_kwh = new_price
        ''' 
        May want to allow total cost to remain unchanged, only allowing the updated price to affect the energy 
        collected after the price is updated.
        '''

    # Method to take the total and the price of energy and calculate the total amount of money saved so far
    def update_money_saved(self):
        total = self.total_kwh
        self.money_saved += (total + self.total_kwh)  * self.price_per_kwh
        # Push the new value for money saved to the front end and server

    # Method used to get an estimate of the current energy being produced for the gauge panel
    def get_current(self):
        current = self.total_kwh - 0
        # Replace the 0 above with a query to the database to get the total from the panels before the latest update
        # Push the value 'current' to the front end to be used as the value displayed by the gauge panel
