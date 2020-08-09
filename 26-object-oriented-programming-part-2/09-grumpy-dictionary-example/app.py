# * Grumpy Dictionary Example

class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR DUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY")
        print("OK FINE....")
        return super().__setitem__(key, value)

    def __contains__(self, key):
        print("NO IT AIN'T IN HERE")


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = "SF"
print(data)
'city' in data
