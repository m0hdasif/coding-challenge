# https://www.codingninjas.com/codestudio/problems/allocate-books_1090540

# return max number of page can be assigned to evenly distribute(minimum difference) and book distribution
def allocate_books(
    books: list[int], no_of_students: int
) -> tuple[int, list[int]]:
    if len(books) < no_of_students:
        raise ValueError("Not all students can get the book")
    start = books[0]
    end = sum(books)
    max_page = -1
    while start <= end:
        mid = start + (end - start) // 2
        if is_possible_to_allocate(books, no_of_students, mid):
            max_page = mid
            end = mid - 1
        else:
            start = mid + 1
    book_distributions = get_book_distribution(books, max_page)
    return max_page, book_distributions


def get_book_distribution(books, max_page):
    book_distributions = [0]
    for book in books:
        if book_distributions[-1] + book <= max_page:
            book_distributions[-1] += book
        else:
            book_distributions.append(book)
    return book_distributions


def is_possible_to_allocate(books: list[int], no_of_students: int, mid):
    no_of_allocated_students = 1
    no_of_allocated_pages = 0
    for book_pages in books:
        if no_of_allocated_pages + book_pages <= mid:
            no_of_allocated_pages += book_pages
        else:
            no_of_allocated_students += 1
            if (no_of_allocated_students) > no_of_students or book_pages > mid:
                return False
            no_of_allocated_pages = book_pages
    return True


if __name__ == "__main__":

    print(f"{allocate_books([10, 20, 30 ,40, 50 ,60],4)=}")
