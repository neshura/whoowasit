#! /usr/bin/python

# dragon goat rockinghorse snake owl boar donkey dog peacock horse

# cheese carrot pear bread cherries nuts grapes mushrooms apple

import random


class Room(object):
    def __init__(self, *static_settings, **kwargs):
        for dictionary in static_settings:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
            
        self._enabled = True
        self._hidden_food = ''
        self._hidden_key = False
        self._animal_eats = ''
        self._thief = False

    @property
    def enabled(self):
        return self._enabled
    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def hidden_food(self):
        return self._hidden_food
    @hidden_food.setter
    def hidden_food(self, value):
        self._hidden_food = value
    
    
    @property
    def hidden_key(self):
        return self._hidden_key
    @hidden_key.setter
    def hidden_key(self, value):
        self._hidden_key = value

    @property
    def animal_eats(self):
        return self._animal_eats
    @animal_eats.setter
    def animal_eats(self, value):
        self._animal_eats = value

    @property
    def thief(self):
        return self._thief
    @thief.setter
    def thief(self, value):
        self._thief = value
    
    
    
        
class Cat(object):
    def __init__(self):
        self._food = list()
        self._key = False

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        self._key = value

    @property
    def food(self):
        return self._food
    @food.setter
    def food(self, value):
        self._food = value
    
    
    def add_key(self):
        if self.key:
            return False
        else:
            self.key = True
            return True


    def rem_key(self):
        if self.key:
            self.key = False
            return True
        else:
            return False

    def add_food(self, items):
        if type(items) is list and len(items) + len(self.food) <= 2:
            for x in items:
                if x not in self.food:
                    self.food.append(x)
                    return True
                else:
                    return False
        elif type(items) is str and len(self.food) <= 1:
            if items not in self.food:
                self.food.append(items)
                return True
            else:
                return False
        else:
            return False

    def remove_food(self, items):
        pass


class Castle(object):
    board = [
        { 'name': 'chapel'    , 'animal': 'snake'  , 'suspect': 'person' },
        { 'name': 'tower'     , 'animal': 'owl'    , 'suspect': 'person' },
        { 'name': 'stables'   , 'animal': 'horse'  , 'suspect': 'person' },
        { 'name': 'courtyard' , 'animal': 'peacock', 'suspect': 'person' },
        { 'name': 'blacksmith', 'animal': 'donkey' , 'suspect': 'person' },
        { 'name': 'armory'    , 'animal': 'boar'   , 'suspect': 'person' },
        { 'name': 'greathall' , 'animal': 'dog'    , 'suspect': 'person' },
        { 'name': 'dungeon'   , 'animal': 'dragon' , 'suspect': 'person' },
        { 'name': 'kitchen'   , 'animal': 'goat'   , 'suspect': 'person' },
    ]
    food = "cheese carrot pear bread cherries nuts grapes mushrooms apple".split()
    def __init__(self, difficulty='easy'):
        self._difficulty = difficulty
        self.rooms = list()
        for static_room in Castle.board:
            room = static_room['name'] 
            setattr(self, room, 
                    Room(static_room,
                        magic = room in ('diningroom', 'stable', 'blacksmith', 'dungeon', 'tower'),
                        trapdoor = room in ('chapel', 'kitchen', 'tower'),
                        pantry = room in ('kitchen'),
                        ravennest = room in ('court'),
                        home = room in ('nursery'),
                        ))
            self.rooms.append(getattr(self, room))

        if self.difficulty is 'easy':
            self.dungeon.enabled = False
            self.tower.enabled = False

        random.shuffle(Castle.food)
        for i, room in enumerate(self.rooms):
            if room.enabled:
                room.hidden_food = Castle.food[i]

        random.shuffle(Castle.food)
        for i, room in enumerate(self.rooms):
            if room.enabled:
                room.animal_eats = Castle.food[i]
        for i in random.sample(self.rooms, 4):
            i.hidden_key = True
        for i in random.sample(self.rooms, 1):
            i.thief = True

    @property
    def difficulty(self):
        return self._difficulty
    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

   
# main
castle = Castle()
meow = Cat()
print '{: <12}{: ^12}{: ^12}{: ^12}{: >12}'.format("name","food","eats" ,"thief","key")
for i in castle.rooms:
    print '{: <12}{: ^12}{: ^12}{: ^12}{: >12}'.format(i.name,i.hidden_food,i.animal_eats,i.thief, i.hidden_key)

print "CLUES:"

# cook
# The thief is tall
# The thief wears a hat
# the thief is a woman
# The thief is carrying something


    








