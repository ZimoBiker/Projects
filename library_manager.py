class LibraryManager:

    def __init__(self, db_path):
        self.db_path = db_path

    def print_header(self):
        print(f'{20 * "*"} WELCOME TO LIBRARY {20 * "*"}')
        print(f"****** Now using the library database in: {self.db_path} ******")

    def display_database(self):
        with open(self.db_path, "r") as db_file:
            lines = [line.strip() for line in db_file.readlines()]
            print("\nBOOKS IN CURRENT DATABASE: \n\n" + "\n".join(lines) + "\n")

    def add_book_to_database(self, book: str):
        with open(self.db_path, "a") as db_file:
            db_file.writelines(book + "\n")
        print(f"\nYour book has been added!\n")

    def sort_the_database(self):
        try:
            with open(self.db_path, "r") as db_file:
                lines = db_file.readlines()

                valid_lines = [
                    line for line in lines if line.strip() and len(line.split("//")) > 2
                ]
                sorted_lines = sorted(
                    valid_lines, key=lambda line: int(line.split("//")[-2].strip())
                )

            with open(self.db_path, "w") as db_file:
                db_file.writelines(line for line in sorted_lines)

        except Exception as e:
            print(f"Error sorting the database: {e}")

    def exit_library(self):
        print("\nGood Bye, Have a nice day!\n")
