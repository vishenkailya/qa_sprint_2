test.py Тестирует класс BooksCollector  
Используется библиотека pytest
test_add_new_book_add_two_books: Добавляем 2 книги  
test_set_book_rating_to_book_not_in_list_none_rating: Получаем рейтинг книг, которых нет в списке      
test_set_book_rating_outside_rating_equals_1: Добавляем книгу с рейтингом больше 10   
test_set_book_rating_in_range_true: Добавляем книгу с рейтингом в диапазоне от 1 до 10    
test_get_book_rating_not_in_list_none: Узнаём рейтинг книги не из списка  
test_get_book_with_specific_rating_above_range_empty_massive: Узнаём список книг с рейтингом вне диапазона      
test_get_book_with_specific_rating_get_one_book: Узнаём книгу с рейтингом 7  
test_add_book_in_favorites_one_book: Добавляем книгу в избранное  
test_add_book_in_favorites_one_book_not_in_books_list: Добавляем в избранное книгу не из списка  
test_delete_boor_from_favorites_empty_list: Удаляем книгу из избранных из пустого списка  
test_delete_boor_from_favorites_that_are_not_in_list_none_result: Удаляем книгу из избранных, которой там нет  