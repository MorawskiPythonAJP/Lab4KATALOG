
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

def search_by_name_or_year():
    value, attribute = read_name_year("Wprowadź nazwę lub rok(pozostaw puste pole by wrócić do menu)")
    if value is None:
        print("Powrót do menu")
        return
    else:
        for item in zasoby:
            if item.get(attribute) == value:
                display_item(item)

def display_item(item):
    print(item['nazwa'])
    print(item['rok'])
    print("Tagi:")
    for tag in item['tagi']:
        print(tag)
    print("\n")

def display_catalog():
    print("Myśliwce w katalogu:")
    for item in zasoby:
        display_item(item)

def display_all_tags():
    all_tags = set()

    for item in zasoby:
        all_tags.update(item['tagi'])
    print("Wszystkie tagi:")
    for tag in all_tags:
        print(tag)

def get_by_tag(prompt):
    print(prompt)
    input_ = input()
    if len(input_) == 0 :
        return None
    requested_items = []
    for item in zasoby:
        if input_ in item.get('tagi'):
            requested_items.append(item)
    return requested_items

def search_by_tag():
    requested_items = get_by_tag("Wprowadź tag(pozostaw puste pole by wrócić do menu)")
    if not requested_items is None:
        for item in requested_items:
            display_item(item)

def main():
    try:
        print("Wybierz opcje")
        print("1 - Wyświetl cały katalog")
        print("2 - Wyszukaj zasób po tytule lub roku")
        print("3 - Wyświetl wszystkie unikalne tagi")
        print("4 - Znajdź zasoby z danym tagiem")
        print("5 - Wyświetl zasoby mające dwa wskazane tagi")
        print("6 - Utwórz nową listę zasobów")
        print("0 - Wyjdź z programu")
        option_index = int(input())
    except ValueError:
        print("Wprowadzona wartość jest nie prawidłowa")
        main()
    else:
        if option_index == 1:
            display_catalog()
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
            main()
        elif option_index == 6:
            main()
        elif option_index == 0:
            print("Wyłączanie programu")
        else:
            print("Wprowadzona wartość jest nie prawidłowa")
            main()

# Nadrzędny wątek

main()