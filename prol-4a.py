from pyswip import Prolog

prolog = Prolog()

#проверить не является ли список А концом списка Б
prolog.assertz("reverce([], []) :- !")
prolog.assertz("reverce([L|[]], [L]) :- !")
prolog.assertz("reverce([H|T], Res) :- reverce(T, R1), append(R1, [H], Res)")

prolog.assertz("dif([], [])")
prolog.assertz("dif([], L)")
prolog.assertz("dif([H1|T1], [H2|T2]) :- H1 == H2, dif(T1, T2) ")


prolog.assertz("tail([], [], t)")
prolog.assertz("tail(L1, L2, t) :- reverce(L1, R1), reverce(L2, R2), dif(R1, R2)")


results = list(prolog.query("tail([1, 2, 3], [5, 5, 5, 5, 1, 2, 3], Res2)"))
for result in results:
    print(f"{result['Res2']}")
