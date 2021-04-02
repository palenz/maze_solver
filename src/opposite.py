import time

def opposites(direction):
    if direction == 'north':
        return 'south'
    elif direction == 'south':
        return 'north'
    elif direction == 'east':
        return 'west'
    elif direction == 'west':
        time.sleep(1)
        return 'east'
        


a= 'west'
print(opposites(a))