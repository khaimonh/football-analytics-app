from .api_interface import api_interface

class testClient(api_interface):
    def __init__(self, fixtures, standings):
        self.fixtures = fixtures 
        self.standings = standings

    def get_fixtures(self):
        return self.fixtures
    def get_standings(self):
        return self.standings