import manipulator
class Controller:
    #test comment for commit purposes
    # Responds to a new websocket channel being opened
    def open_channel(self):
        # Send the data that is required by the new channel
        '''
        Given the set default timescale, query the database and forward that data to the websocket, for the user to view
        :return:
        '''
        print('implement open_channel')

    # Push updated data to all websocket clients every ten minutes
    def update_channels(self):
        '''
        Each time that new data is gathered push it along all open channels so thateach has access to the
        new information
        :return:
        '''
        print('implement update_channels')

    # Query SQL database for data in the given timescale.
    def get_data (timescale):
        '''
        Given the new timescale (year, month, week, or day) create a query to the database to retrieve the data for the
        specified period
        :return:
        '''
        print('implement get_data')

    # Responds to a client's request to change the timescale that they are viewing
    def change_timescale(new_timescale):
        '''
        given the new timescale, call get_data(timescale) to create a query for the database structured to retrieve
            that time frame
        update websocket channels to reflect the new time frame, while allowing other websocket channels to
            remain unaltered
        :return:
        '''
        print('implement chenge_timescale')

    # Allows admins to login
    def login(username, password):
        '''
        Look up  username in SQL Database and check that the password for that username entry matches
        the password provided
        '''
        '''
        if in_database(username):
            if pass_match(username, password):
                go to admin page
        else 
            display(invalid username/password
        '''
        print('implement login')

    # Parses updates from the dashboard editor and updates the values in the database
    def update_admin_settings(self):
        '''
        parse info given by the front end
        find user in database
        save to database (only save if values are different)
        :return:
        '''
        print('implement update_admin_settings')

