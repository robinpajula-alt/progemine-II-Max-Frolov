class Diary:
    def __init__(self):
        self.sissekanded = []
        self.loendur = 0

    def add_entry(self, text):
        self.loendur = self.loendur + 1
        sissekanne = str(self.loendur) + ": " + text #siin peaks muutma
        self.sissekanded.append(sissekanne)

    def remove_entry(self, index):
        self.sissekanded.pop(index)

    def __str__(self):
        return "\n".join(self.sissekanded)