class PrinterSpy:
    def print_item(self, item):
        self.printed_item = item

    def printed(self):
        return self.printed_item
