'''
#Versión inicial
def search_courses(query: str) -> list[str]:
    titles = ["Python foundations", "Python for data analysis", "Machine learning introduction"]
    matches = []
    for title in titles:
        if query.strip().casefold() in title.casefold():
            matches.append(title)
    return matches


def main() -> None:
    print(search_courses("python"))


if __name__ == "__main__":
    main()

# Versión con logging
from catalog.search import search_courses
import logging

def main() -> None:
    logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(name)s | %(message)s",
    )
    for course in search_courses("python"):
        print(course.model_dump_json())



#Mensajes con INFO
#INFO | catalog.search | Search completed: 2 matches
#{"code":"PY01","title":"Python foundations","hours":12}
#{"code":"PY02","title":"Python for data analysis","hours":16}

if __name__ == "__main__":
    main()

'''
