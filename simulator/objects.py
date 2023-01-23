class Object:
    
    def __init__(self):
        self.state = None
        
    def __update(self, obs):
        pass
        
    def update(self):
        obs = self.get_observation()
        
        self.__update(self, obs)
        
    def get_observation(self):
        return self.state.objects