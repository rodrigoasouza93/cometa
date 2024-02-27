class ListBeersController:
    def __init__ (self, listBeers):
        self.listBeers = listBeers
    
    def handle(self):
        return self.listBeers.execute()