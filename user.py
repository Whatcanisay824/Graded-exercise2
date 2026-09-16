from admin import (
    load_library,
    save_library,
    find_book
)


def books_in_category(books, category):
    category = category.strip().lower()
    result = []
    for book_id in books:
        if books[book_id]["category"].lower() == category:
            result.append(book_id)
    return result


def search_by_title(books, search_text):
    search_text = search_text.strip().lower()
    result = []
    for book_id in books:
        if search_text in books[book_id]["title"].lower():
            result.append(book_id)
    return result


def borrow_book(books, loans, search_text, borrower):
    if borrower.strip() == "":
        return "EMPTY_NAME"
    book_id = find_book(books, search_text)
    if book_id is None:
        return "BOOK_NOT_FOUND"
    if books[book_id]["available"] == False:
        return "NOT_AVAILABLE"
    books[book_id]["available"] = False
    loans.append({"book_id": book_id, "borrower": borrower})
    return "OK"


def return_book(books, loans, book_title, borrower):
    if borrower.strip() == "":
        return "EMPTY_NAME"
    book_id = find_book(books, book_title)
    if book_id is None:
        return "BOOK_NOT_FOUND"
    found = None
    for loan in loans:
        if loan["book_id"] == book_id:
            found = loan
            break
    if found is None:
        return "NOT_ON_LOAN"
    loans.remove(found)
    books[book_id]["available"] = True
    return "OK"


def main():
    data = load_library("library.json")
    books = data["books"]
    loans = data["loans"]

    print("LIBRARY USER SYSTEM")
    print("=" * 60)

    while True:
        print()
        print("1. Search by title")
        print("2. Search by category")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter title to search: ")
            results = search_by_title(books, text)
            if len(results) == 0:
                print("No books found.")
            else:
                for book_id in results:
                    print(book_id, "|", books[book_id]["title"], "|", books[book_id]["category"])

        elif choice == "2":
            text = input("Enter category to search: ")
            results = books_in_category(books, text)
            if len(results) == 0:
                print("No books found.")
            else:
                for book_id in results:
                    print(book_id, "|", books[book_id]["title"], "|", books[book_id]["category"])

        elif choice == "3":
            text = input("Enter book ID or title: ")
            name = input("Enter your name: ")
            result = borrow_book(books, loans, text, name)
            if result == "OK":
                print("Book borrowed successfully.")
            elif result == "EMPTY_NAME":
                print("Borrower name cannot be empty.")
            elif result == "BOOK_NOT_FOUND":
                print("Book not found.")
            elif result == "NOT_AVAILABLE":
                print("Book is not available.")

        elif choice == "4":
            text = input("Enter book ID or title: ")
            name = input("Enter your name: ")
            result = return_book(books, loans, text, name)
            if result == "OK":
                print("Book returned successfully.")
            elif result == "EMPTY_NAME":
                print("Borrower name cannot be empty.")
            elif result == "BOOK_NOT_FOUND":
                print("Book not found.")
            elif result == "NOT_ON_LOAN":
                print("This book is not on loan.")

        elif choice == "5":
            save_library(data, "library.json")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()