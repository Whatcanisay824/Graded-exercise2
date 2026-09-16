import json


def load_library(filename):
    f = open(filename, "r")
    data = json.load(f)
    f.close()
    return data


def save_library(data, filename):
    f = open(filename, "w")
    json.dump(data, f, indent=4)
    f.close()


def find_book(books, search_text):
    search_text = search_text.strip().lower()
    for book_id in books:
        book = books[book_id]
        if book_id.lower() == search_text:
            return book_id
        if book["title"].lower() == search_text:
            return book_id
        if book["author"].lower() == search_text:
            return book_id
    return None


def display_books(books):
    print()
    print("BOOK CATALOGUE")
    print("-" * 60)
    for book_id in books:
        book = books[book_id]
        if book["available"]:
            status = "AVAILABLE"
        else:
            status = "ON LOAN"
        print(book_id, "|", book["title"], "|", book["category"], "|", status)


def display_loans(loans, books):
    print()
    print("CURRENT LOANS")
    print("-" * 60)
    for loan in loans:
        book_id = loan["book_id"]
        if book_id in books:
            print(book_id, "|", books[book_id]["title"], "| Borrower:", loan["borrower"])


def library_statistics(books):
    total = len(books)
    available = 0
    for book_id in books:
        if books[book_id]["available"]:
            available = available + 1
    borrowed = total - available
    return (total, available, borrowed)


def main():
    data = load_library("library.json")
    books = data["books"]
    loans = data["loans"]
    library = data["library"]
    categories = data["categories"]

    print("LIBRARY ADMINISTRATION")
    print("=" * 60)
    print("Library:", library["name"])
    print("Branch:", library["branch"])
    print("Year:", library["year"])
    print("Categories:", ", ".join(categories))

    display_books(books)
    display_loans(loans, books)

    total, available, borrowed = library_statistics(books)

    print()
    print("STATISTICS")
    print("-" * 60)
    print("Total books:", total)
    print("Available:", available)
    print("Borrowed:", borrowed)


if __name__ == "__main__":
    main()