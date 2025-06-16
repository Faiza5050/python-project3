import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    print("\nAdd a Book")
    title = input('Enter The Book Title: ')
    author = input('Enter The Author: ')
    year = input('Enter The Publication Year: ')
    genre = input('Enter The Genre: ')
    read_input = input('Have You Read This Book? (yes/no): ').lower()
    read = True if read_input == 'yes' else False

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print('Book Added Successfully!')

def remove_book(library):
    print("\nRemove a Book")
    title = input('Enter the title of the book to remove: ')
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]
    
    if len(library) < initial_length:
        save_library(library)
        print('Book Removed Successfully!')
    else:
        print('Book not Found!')

def search_for_book(library):
    print("\nSearch for a Book")
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter Your Choice: ")

    if choice == '1':
        term = input("Enter The Title: ").strip().lower()
        results = [book for book in library if term in book['title'].lower()]
    elif choice == '2':
        term = input("Enter The Author: ").strip().lower()
        results = [book for book in library if term in book['author'].lower()]
    else:
        print("Invalid Choice.")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, start=1):
            status = 'Read' if book['read'] else 'Unread'
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_all_books(library):
    print("\nYour Library:")
    if library:
        for i, book in enumerate(library, start=1):
            status = 'Read' if book['read'] else 'Unread'
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("The Library is Empty.")

def display_statistics(library):
    print("\nLibrary Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total Books: {total_books}")
    print(f"Percentage Read: {percentage_read:.2f}%")

def main():
    library = load_library()

    while True:
        print("\nWelcome To Your Personal Library Manager!\n")  
        print("1. Add a Book")  
        print("2. Remove a Book")  
        print("3. Search for a Book")  
        print("4. Display all Books")  
        print("5. Display Statistics")  
        print("6. Exit")  
        choice = input("Enter Your Choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_for_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library Saved to file. Goodbye!")
            break
        else:
            print("Invalid Choice. Please Try Again.")

if __name__ == '__main__':
    main()
