from pyswip import Prolog

prolog = Prolog()

#3b проверить, является ли длина списка нечетной odd(Lst， result)

prolog.assertz("odd([], false)")
prolog.assertz("odd([H | []], true)")
prolog.assertz("odd([H|[T1| T2]], Res) :- odd(T2, Res)")


results = list(prolog.query("odd([1, 2, 3], Res)"))


for result in results:
    print(f"{result['Res']}")