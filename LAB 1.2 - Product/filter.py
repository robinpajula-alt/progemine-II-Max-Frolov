class BetterFilter:
    def filter(self, products, specification):
        for product in products:
            if specification.is_satisfied(product):
                yield product