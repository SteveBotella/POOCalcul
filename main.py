class CalculSurListe:

    def __init__(self, number_list):
        self.number_list = number_list

    def calculer(self):
        return self._effectuercalcul()

    # _effectuercalcul correspond a protected ( __ pour private)
    def _effectuercalcul(self):
        raise Exception("not implemented")
        return sum(self.number_list)


class CalculSurListeSomme(CalculSurListe):
    def __init__(self, number_list):
        super().__init__(number_list[0:2])

    def _effectuercalcul(self):
        return sum(self.number_list)

class CalculSurListeSommeNegative(CalculSurListe):

    def _effectuercalcul(self):
        return 0 - sum(self.number_list)

if __name__ == '__main__':
    c = CalculSurListeSomme([1, 2, 3, 4])
    d = CalculSurListeSommeNegative([5, 6, 7])
    e = CalculSurListe([5, 6, 7])
    print(c.number_list)
    print(d.number_list)
    print(c.calculer())
    print(d.calculer())
    # c = CalculSurListeSomme([1, 2, 3, 4])
    # print(c.calculer())
    # c = CalculSurListeProduit([1, 2, 3, 4])
    # print(c.calculer())
