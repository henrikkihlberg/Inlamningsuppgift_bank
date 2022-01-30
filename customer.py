

class customer:
    def __init__(self, customer_id, name, pnr, *args):
        self.customer_id = int(customer_id)
        self.name = name
        self.pnr = int(pnr)
        for x in range(len(args)):
            self.account = args[x]

