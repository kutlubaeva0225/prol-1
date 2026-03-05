from pyswip import Prolog

prolog = Prolog()

#[1A]
# Добавляем факты в базу знаний  parent(parent, child)
prolog.assertz("parent(alice, charlie)")
prolog.assertz("parent(alice, diane)")
prolog.assertz("parent(bob, charlie)")
prolog.assertz("parent(bob, diane)")
prolog.assertz("parent(emily, gregory)")
prolog.assertz("parent(emily, harry)")
prolog.assertz("parent(fred, gregory)")
prolog.assertz("parent(fred, harry)")
prolog.assertz("parent(fred, oscar)")
prolog.assertz("parent(diane, ian)")
prolog.assertz("parent(diane, jack)")
prolog.assertz("parent(diane, kevin)")
prolog.assertz("parent(gregory, ian)")
prolog.assertz("parent(gregory, jack)")
prolog.assertz("parent(gregory, kevin)")
prolog.assertz("parent(kevin, michael)")
prolog.assertz("parent(kevin, norman)")
prolog.assertz("parent(linda, michael)")
prolog.assertz("parent(linda, norman)")

prolog.assertz("woman(alice)")
prolog.assertz("woman(diane)")
prolog.assertz("woman(emily)")
prolog.assertz("woman(linda)")
prolog.assertz("man(bob)")
prolog.assertz("man(fred)")
prolog.assertz("man(charlie)")
prolog.assertz("man(gregory)")
prolog.assertz("man(kevin)")
prolog.assertz("man(michael)")
prolog.assertz("man(norman)")
prolog.assertz("man(ian)")
prolog.assertz("man(jack)")
prolog.assertz("man(harry)")
prolog.assertz("man(oscar)")

prolog.assertz(r"sister(X, Y) :- parent(Z, X), parent(Z, Y), woman(X), X \= Y")
prolog.assertz("aunt(X, Y) :- parent(Z, Y), sister(X, Z)")
prolog.assertz("niece(X, Y) :- aunt(Y, X), woman(X)")

# Делаем запрос: кто дети Ивана?
results = list(prolog.query("aunt(X, Y), niece(Y, X)"))


for result in results:
    print(f"Тетя -  {result['X']}", f"Племянница - {result['Y']}")