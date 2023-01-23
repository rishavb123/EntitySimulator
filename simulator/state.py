import time

class State:
    
    def __init__(self):
        self.objects = set()
        
    def add_object(self, obj):
        self.objects.add(obj)
        obj.state = self
        
    def update(self):
        for obj in self.objects:
            obj.update()
            
    def run(self, fps=30, num_frames=1000):
        frame_counter = 0
        delay = 1 / fps
        last_time = time.time()
        while frame_counter < num_frames:
            cur_time = time.time()
            if cur_time - last_time < delay: continue
            last_time = cur_time
            
            frame_counter += 1
            
            print(f"Running frame {frame_counter}")
            
            self.update()