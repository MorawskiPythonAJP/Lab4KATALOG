
zasoby = [
    {
        "nazwa": "F-14",
        "rok": "1970",
        "tagi" : {"USA", "I", "GEN4"}
    },
    {
        "nazwa": "Rafale",
        "rok": "1986",
        "tagi" : {"FR", "MR", "GEN4"}
    },
    {
        "nazwa": "F-35",
        "rok": "2006",
        "tagi" : {"USA", "MR", "GEN5"}
    },
    {
        "nazwa": "F-22",
        "rok": "1990",
        "tagi" : {"USA", "AS", "GEN5"}
    },
    {
        "nazwa": "Mig-31",
        "rok": "1977",
        "tagi" : {"ZSRR", "I", "GEN4"}
    },
    {
        "nazwa": "Su-27",
        "rok": "1982",
        "tagi" : {"ZSRR", "AS", "GEN4"}
    },
]

zasoby_2 = []

# Czytanie roku lub nazwy szukanego przedmiotu od użytkownika
def read_name_year(prompt):
    print(prompt)
    input_ = input()
    if len(input_) == 0 :
        return None, None
    try:
        int(input_)
    except ValueError:
        return input_, "nazwa"
    else:
        return input_, "rok"

# Dalsza walidacja i tworzenie listy przedmiotów z szukaną datą lub nazwą
def group_by_name_year(source):
    value, attribute = read_name_year("Wprowadź nazwę lub rok(pozostaw puste pole by wrócić do menu)")
    return_list = []
    if value is None:
        print("Powrót do menu")
        return return_list
    else:
        for item in source:
            if item.get(attribute) == value:
                return_list.append(item)
        return return_list

# Nadrzędna funkcja zajmująca się szukaniem rzeczy po dacie lub nazwie
def search_by_name_or_year():
    filtered = group_by_name_year(zasoby)
    display_catalog(filtered)

# Wyświetl pojedyńczy przedmiot
def display_item(item):
    print(item['nazwa'])
    print(item['rok'])
    print("Tagi:")
    for tag in item['tagi']:
        print(tag)
    print("\n")

# Wyświetl daną listę przedmiotów
def display_catalog(source):
    if not len(source) == 0:
        print("Myśliwce w katalogu:")
        for item in source:
            display_item(item)

# Wyświetl wszystkie możliwe tagi
def display_all_tags():
    all_tags = set()

    for item in zasoby:
        all_tags.update(item['tagi'])
    print("Wszystkie tagi:")
    for tag in all_tags:
        print(tag)

# Czyta tag wprowadzony do użytkownika i zwraca wszystkie pasujące elementy
def get_by_tag(prompt, source):
    print(prompt)
    requested_items = []
    input_ = input()
    if len(input_) == 0 :
        return requested_items
    for item in source:
        if input_ in item.get('tagi'):
            requested_items.append(item)
    return requested_items

# Nadrzędna funkcja szukająca i wyświetlająca przedmioty z jednym podanym tagiem
def search_by_tag():
    requested_items = get_by_tag("Wprowadź tag(pozostaw puste pole by wrócić do menu)", zasoby)

    for item in requested_items:
        display_item(item)

# Nadrzędna funkcja szukająca i wyświetlająca przedmioty z dwoma podanymi tagami
def search_by_two_tags():
    first_tag_items = get_by_tag("Wprowadź tag(pozostaw puste pole by wrócić do menu)", zasoby)
    if not first_tag_items is None:
        requested_items = get_by_tag("Wprowadź tag(pozostaw puste pole by wrócić do menu)", first_tag_items)
        print(requested_items)
        if not requested_items is None:
            for item in requested_items:
                display_item(item)

# Tworzenie nowej kolekcji na podstawie podanych warunków
def add_new_condition(source):
    print("Wskaż opcje filtru")
    print("1 - Nazwa lub rok")
    print("2 - Tagi")
    print("0 - Zapisz nowy katalog")
    try:
        option_index = int(input())
    except ValueError:
        print("Wprowadzona wartość jest nie prawidłowa")
        return add_new_condition(source)
    else:
        if option_index == 1:
            filtered = group_by_name_year(source)
            if len(filtered) > 0:
                return add_new_condition(filtered)
            else:
                print("Założony filtr nie pasuje do żadnego elementu, powrót do poprzedniego stanu")
                return add_new_condition(source)
        elif option_index == 2:
            filtered = get_by_tag("Wprowadź tag(pozostaw puste pole by wrócić do menu)", source)
            if len(filtered) > 0:
                return add_new_condition(filtered)
            else:
                print("Założony filtr nie pasuje do żadnego elementu, powrót do poprzedniego stanu")
                return add_new_condition(source)
        elif option_index == 0:
            print("Nowy katalog został zapisany")
            return source
        else:
            print("Wprowadzona wartość jest nie prawidłowa")
            return add_new_condition(source)

# Tworzy nową kolekcję na podstawie istniejącej kolekcji
def create_new_collection():
    entry_collection = zasoby.copy()
    return add_new_condition(entry_collection)

# Prezentacja różnicy między kopią a przypisaniem
def copy_vs_reference_demonstration():
    oryginal = ["Solaris", "Diuna"]
    alias = oryginal
    kopia = oryginal.copy()

    alias.append("Lalka")
    print(oryginal)
    print(kopia)
    print(oryginal is alias)
    print(oryginal == kopia)

# Główna funkcja
def main():
    global zasoby_2

    try:
        print("Wybierz opcje")
        print("1 - Wyświetl cały katalog")
        print("2 - Wyszukaj zasób po tytule lub roku")
        print("3 - Wyświetl wszystkie unikalne tagi")
        print("4 - Znajdź zasoby z danym tagiem")
        print("5 - Wyświetl zasoby mające dwa wskazane tagi")
        print("6 - Utwórz nową listę zasobów")
        print("7 - Wyświetl nową listę zasobów")
        print("8 - Demonstracja różnicy między kopią, a przypisaniem")
        print("0 - Wyjdź z programu")
        option_index = int(input())
    except ValueError:
        print("Wprowadzona wartość jest nie prawidłowa")
        main()
    else:
        if option_index == 1:
            display_catalog(zasoby)
            main()
        elif option_index == 2:
            search_by_name_or_year()
            main()
        elif option_index == 3:
            display_all_tags()
            main()
        elif option_index == 4:
            search_by_tag()
            main()
        elif option_index == 5:
            search_by_two_tags()
            main()
        elif option_index == 6:
            zasoby_2 = create_new_collection()
            main()
        elif option_index == 7:
            display_catalog(zasoby_2)
            main()
        elif option_index == 8:
            copy_vs_reference_demonstration()
            main()
        elif option_index == 0:
            print("Wyłączanie programu")
        else:
            print("Wprowadzona wartość jest nie prawidłowa")
            main()

# Nadrzędny wątek

main()