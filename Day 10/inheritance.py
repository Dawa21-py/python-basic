class GrandFather:
    house = "luxury house"

    def __init__(self) -> None:
        print("luxury")



class Father(GrandFather):
    car = "Ducati"

    def __init__(self) -> None:
        print("newhouse")
        print(self.car)
        super().__init__()


class Mother:
    jellewry = "Diamond"

class son(Father, Mother):
    console = "PS5"

    def __init__(self) -> None:
        print(self.console)
        super().__init__()


# Father = Father()
# print(Father.car)
son = son()
# print(son.jellewry) 