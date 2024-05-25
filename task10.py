class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles
    def sweetness(self):
        bomazza = {"Plain": 0, "Vanilla": 5, "ChocolateChip": 5, "Strawberry": 10, "Chocolate": 10}
        return bomazza[self.flavor] + self.num_sprinkles
    def sweetest_icecream(lst):
        max_sweetness = 0
        for ice in lst:
            sweetness = ice.sweetness()
        if sweetness > max_sweetness:
            max_sweetness = sweetness
            return max_sweetness

list1 = IceCream("Chocolate", 13)
list2 = IceCream("Vanilla", 0)
list3 = IceCream("Strawberry", 5)
list4 = IceCream("Plain", 2)
list5 = IceCream("ChocolateChip", 8)

print(sweetness([list1, list2, list3, list4, list5]))
print(sweetest_icecream([list3, list1]))