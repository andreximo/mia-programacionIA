import logging

from catalog.search import search_courses

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(name)s | %(message)s",
)


def main() -> None:
    for course in search_courses("python"):
        print(course.model_dump_json())


if __name__ == "__main__":
    main()
