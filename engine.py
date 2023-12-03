# default collider
class Collider():
    active_colliders = []

    def __init__(self):
        self.cooldown = 0 # used for problem with multiple collision

    def colision(collider):
        if(collider.cooldown == 0):
            for active_collider in Collider.active_colliders: # check all coliders in map
                if(collider != active_collider):
                    if(active_collider.check_colision(collider)): # if colliding returns the collider
                        collider.cooldown = 2
                        return active_collider
        else:
            collider.cooldown -= 1
        return None


# Rectangular collider
class Box_Collider(Collider):
    def __init__(self, x, y, width, height, object):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.object = object

    def check_colision(self, collider):
        return (self.x - collider.width <= collider.x <= self.x + self.width and self.y - collider.height <= collider.y <= self.y + self.height)