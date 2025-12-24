from collections import deque

class Snake:
    def __init__(self, initial_body = None, initial_dir = (1,0)) -> None:
        if initial_body == None:
            initial_body =  [(5, 5), (4, 5), (3, 5)]
        self.body = deque(initial_body)
        self.direction = initial_dir
        self.next_dir = initial_dir
        self.grow_pending = 0

    def head(self):
        return self.body[0]

    def set_direction(self, new_dir):
        dx, dy = new_dir
        cdx, cdy = self.direction

        if (dx, dy) == (cdx, cdy):
            return
        
        if (dx, dy) == (-cdx, -cdy):
            return
        
        self.next_dir = (dx, dy)
    
    def step(self, rows, cols, walls):
        self.direction = self.next_dir
        
        hx, hy = self.head()
        dx, dy = self.direction
        
        new_head = ((hx + dx), (hy + dy)) if walls else ((hx + dx) % cols, (hy + dy) % rows)
        self.body.appendleft(new_head)

        # if food the dont pop
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def grow(self, n = 1):
        self.grow_pending += n



