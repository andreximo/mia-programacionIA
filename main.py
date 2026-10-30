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