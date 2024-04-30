class ReversedList:

    def __init__(self, array_num):
        self.array_num = array_num

    def __len__(self):
        return len(self.array_num)

    def __getitem__(self, item):
        return self.array_num[-1::-1][item]


rlist = ReversedList([1, 2, 3, 4, 5])
for i in range(len(rlist)):
    print(rlist[i])