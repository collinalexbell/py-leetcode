import random
class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if(val not in self.set):
            self.set[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if(val in self.set):
            index = self.set[val]
            toMove = self.list[len(self.list)-1]
            self.set[toMove] = index
            self.list[index] = toMove
            self.set.pop(val)
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        item = self.list[random.randint(0, len(self.list)-1)]
        return item

