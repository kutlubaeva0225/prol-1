from pyswip import Prolog

prolog = Prolog()
prolog.retractall("copy(_, _)")
#[2Б] дублирование элементов списка



prolog.assertz("copy([],[])")
prolog.assertz(r"copy([H|T], [H, H | R]) :- copy(T, R)")


results = list(prolog.query("copy([1, 2, 3, 4, 5], Lst)"))


for result in results:
    print(f"{result['Lst']}")