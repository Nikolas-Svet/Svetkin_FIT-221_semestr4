class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value

    def __getitem__(self, index):
        return self.data.get(index, 0)


arr = SparseArray()
arr[1] = 10
arr[3] = 20
arr[5] = 0
print(arr[1])
for i in range(8):
    print(arr[i])