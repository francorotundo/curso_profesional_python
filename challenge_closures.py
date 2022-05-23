def make_division_by(n: int):
    #this closure returns a function that returns the division of an x number by n
    def division(x: int):
        assert (type(x) == int or type(x) == float) and x > 0, 'Tiene que usar para la división un valor positivo, mayor a cero.'
        return int(x//n)
    return division

#Other form
# make_division_by = lambda n: lambda x : x//n

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()