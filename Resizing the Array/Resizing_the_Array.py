# arrays.py

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = [fill_value] * capacity

    def __str__(self):
        return str(self.items)
    
    def insert(self, index, value):
        if 0 <= index <= len(self.items):
            self.items = self.items[:index] + [value] + self.items[index:]
        else:
            print(f"Error: Index {index} is out of bounds")

    def delete(self, index):
        if 0 <= index < len(self.items):
            self.items = self.items[:index] + self.items[index+1:]
        else:
            print(f"Error: Index {index} is out of bounds")
    
    def increase_size(self, new_capacity):
        # Increase the size of the array by adding None values
        self.items += [None] * (new_capacity - len(self.items))

    def decrease_size(self, new_capacity):
        # Decrease the size by slicing the list to the new capacity
        self.items = self.items[:new_capacity]


# Testing the Array class with resizing
if __name__ == "__main__":
    arr = Array(5, 0)
    print(arr)  # [0, 0, 0, 0, 0]

    arr.increase_size(8)
    print(arr)  # [0, 0, 0, 0, 0, None, None, None]

    arr.decrease_size(4)
    print(arr)  # [0, 0, 0, 0]

