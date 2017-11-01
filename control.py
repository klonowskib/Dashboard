import manipulator
class Manipulator:
    # Responds to a new websocket channel being opened
    def open_channel(self):
        # Send the data that is required by the new channel
        print('implement open_channel')
    # Push updated data to all websocket clients every ten minutes
    def update_channels(self):
        print('implement update_channels')

    # Query SQL database for data in the given timescale.
    def get_data (timescale):
        print('implement get_data')

    # Responds to a client's request to change the timescale that they are viewing
    def change_timescale(new_timescale):
        print('implement chenge_timescale')

    # Allows admins to login
    def login(username, password):
        print('implement login')

    # Parses updates from the dashboard editor and updates the values in the database
    def update_admin_settings(self):
        print('implement update_admin_settings')
