class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.full = False
    def append(self, item):
        if self.full:
            self.storage[self.oldest_index] = item
            self.oldest_index = (self.oldest_index+1) % self.capacity
        else:
            self.storage.append(item)
            if len(self.storage) == self.capacity:
                self.full = True
                self.oldest_index = 0
    def get(self):
        return self.storage

    #setting variables and starting with false which makes it go to the else,
    #adding to the storage and if the length of the storage matches capacity it sets to true and start the oldest index first
    #and then it moves through the index and checks to see if its moved through all the way