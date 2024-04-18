# Exercice 5: Design Patterns
# Implémentez le modèle de conception Observer. Créez une classe Observable qui peut être surveillée par plusieurs observateurs, et chaque observateur doit réagir aux changements dans l'observable.

class Observable:
    def __init__(self):
        self._observers = set()

    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received message: {message}")

# Exemple d'utilisation
observable = Observable()
observer1 = Observer()
observer2 = Observer()

observable.add_observer(observer1)
observable.add_observer(observer2)

observable.notify_observers("Hello, observers!")
