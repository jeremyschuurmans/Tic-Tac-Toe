class PrinterSpy:
    def __init__(self):
        self.printed_item = ""
        self.printed_items = []

    def print_item(self, item):
        self.printed_item = item
        self.printed_items.append(item)

    def printed(self):
        return self.printed_item
