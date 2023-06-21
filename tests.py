import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_to_book_not_in_list_none_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Capital. Part 2', 10)
        assert collector.get_book_rating('Capital. Part 2') == None

    @pytest.mark.parametrize('rating', [11, 15, 100])
    def test_set_book_rating_above_10_rating_equals_1(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Бойцовский клуб')
        collector.set_book_rating('Бойцовский клуб', rating)
        assert collector.get_book_rating('Бойцовский клуб') == 1

    @pytest.mark.parametrize('rating', [0, -1, -10])
    def test_set_book_rating_lower_1_rating_equals_1(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Бойцовский клуб')
        collector.set_book_rating('Бойцовский клуб', rating)
        assert collector.get_book_rating('Бойцовский клуб') == 1

    @pytest.mark.parametrize('rating', [1, 5, 10])
    def test_set_book_rating_in_range_true(self, rating):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', rating)
        assert collector.get_book_rating('1984') == rating

    def test_get_book_rating_not_in_list_none(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Fire Punch') == None

    @pytest.mark.parametrize('rating', [11, 15, 100])
    def test_get_book_with_specific_rating_above_range_empty_massive(self, rating):
        collector = BooksCollector()
        assert collector.get_books_with_specific_rating(rating) == []

    def test_get_book_with_specific_rating_get_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('1985')
        collector.set_book_rating('1985', 7)
        assert collector.get_books_with_specific_rating(7) == ['1985']

    def test_get_book_with_specific_rating_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Берсерк')
        collector.add_new_book('Overlord')
        collector.set_book_rating('Берсерк', 10)
        collector.set_book_rating('Overlord', 10)
        assert len(collector.get_books_with_specific_rating(10)) == 2

    def test_get_books_rating_2_books(self):
        collector = BooksCollector()
        collector.add_new_book('Rage')
        collector.add_new_book("Dante's Inferno")
        collector.set_book_rating('Rage', 6)
        collector.set_book_rating("Dante's Inferno", 9)
        assert len(collector.get_books_rating()) == 2

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Бойцовский клуб')
        collector.add_book_in_favorites('Бойцовский клуб')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_one_book_not_in_books_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('1+1')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_boor_from_favorites_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('1+1')
        collector.add_book_in_favorites('1+1')
        collector.delete_book_from_favorites('1+1')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_boor_from_favorites_that_are_not_in_list_none_result(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('1+1')
        assert collector.get_list_of_favorites_books() == []

