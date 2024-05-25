class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner
    def winners(self):
        return f"Nobel Prize in {self.category} ({self.year}): {self.winner}"

num = Nobel("Peace", 2005, "Muhammad Yunus")
print(num)