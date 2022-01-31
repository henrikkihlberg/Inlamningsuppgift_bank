

class customer:
    def __init__(self, _id, name, pnr, *args):
        self._id = int(_id)
        self.name = name
        self.pnr = int(pnr)
        for x in range(len(args)):
            self.account = args[x]

