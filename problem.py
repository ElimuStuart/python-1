books = [
    "The Lord of The Rings", "The Hobbit", "Harry Potter and the Chamer of Secrets",
    "Black Beauty", "Kane and Abel", "To Kill a Mocking Bird", "Rumi Poems"
]

book_catalog = {} 

for book in books:
    book_index = book[0] # extract the first letter (for catalog)
    if book_index not in book_catalog:
        book_catalog[book_index] = [book]
    else:
        book_catalog[book_index].append(book) # append book if index already exists

print(book_catalog)