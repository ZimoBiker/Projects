import sys
from library_manager import LibraryManager
from os import path


def main(*args):

    if len(sys.argv) != 2:
        handle_parameter_error()

    db_path = sys.argv[1]
    lib_manager = LibraryManager(db_path)

    if not path.exists(db_path):
        handle_parameter_error()

    else:
        lib_manager.print_header()

    while True:
        choice = ""
        while choice.lower() not in ["1", "2", "q"]:
            choice = input(
                """
            Please choose one of the following options:
            
            1 - Add a new book to the database
            2 - Print the current database
            Q - Quit the program
            
            Enter your choice (1, 2, or Q):
            """
            )
        match choice.lower():
            case "1":
                name = input("Please enter the name of the book: ").strip()
                author = input("Please enter the author of the book: ").strip()
                isbn = input("Please enter the ISBN of the book: ").strip()
                year = input("Please enter the year the book was published: ").strip()
                book = f"//{name}//{author}//{isbn}//{year}//"
                while True:
                    add = ""
                    while add.lower() not in ("y", "n"):
                        add = input(
                            f"\nDo you wish to add book with information: \n {book} "
                            f"to the database? (Yes(y), No(n))\n"
                        )

                    if add == "y":
                        lib_manager.add_book_to_database(book)
                        lib_manager.sort_the_database()
                        break
                    else:
                        break

            case "2":
                lib_manager.display_database()
            case "q":
                lib_manager.exit_library()
                break
        if choice == "Q":
            break


def handle_parameter_error():
    print(
        "\nUsage: python main.py <path_to_database>\n",
        "\nPlease make sure your path is correct and you have the necessary permissions\n",
    )
    sys.exit()


if __name__ == "__main__":
    main()
