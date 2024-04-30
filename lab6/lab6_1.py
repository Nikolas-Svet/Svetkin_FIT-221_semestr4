class BigBell:
    def __init__(self):
        self.flag = True

    def sound(self):
        if self.flag:
            print("ding")
            self.flag = False
        else:
            print("dong")
            self.flag = True


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()