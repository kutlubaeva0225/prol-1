from pyswip import Prolog

prolog = Prolog()


#5b, make_list(List, Res)

prolog.assertz("make_list([], []):- !")
prolog.assertz(r"make_list(N, [N]):- \+ is_list(N)")
prolog.assertz("make_list([H|T], Res) :- make_list(H, R1), make_list(T, R2), append(R1, R2, Res)")

results = list(prolog.query("make_list([[1], [2, 3], 3], Res)"))


for result in results:
    print(f"{result['Res']}")