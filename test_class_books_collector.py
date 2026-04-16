import pytest


from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name',['','a'*41,'Мемуары придворного карлика гностика по убеждениям'])
    def test_add_new_book_invalid_name_not_added(self,name,collector):
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_add_new_book_not_add_double(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    def test_get_book_genre_adding_book_to_genre(self,collector):
        collector.add_new_book('1+1')
        collector.set_book_genre('1+1','Комедии')
        assert collector.get_book_genre('1+1') == 'Комедии'

    def test_set_book_genre_not_sets_genre(self,collector):
        collector.add_new_book('1+1')
        assert collector.get_book_genre('1+1') == ''

    def test_get_books_with_specific_genre_returns_books(self,collector):
        collector.add_new_book('Собака Баскервилей')
        collector.set_book_genre('Собака Баскервилей','Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Собака Баскервилей']

    def test_get_books_with_specific_genre_not_genre_empty_list(self,collector):
        collector.add_new_book('Собака Баскервилей')
        assert collector.get_books_with_specific_genre('Мемуары') == []

    def test_get_books_with_specific_genre_not_book_empty_list(self,collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []
    
    def test_get_books_genre_returns_dict(self,collector):
        collector.add_new_book('Собака Баскервилей')
        collector.set_book_genre('Собака Баскервилей','Детективы')
        assert collector.get_books_genre() == {'Собака Баскервилей':'Детективы'}

    def test_get_books_for_children_returns_allowed_book(self,collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Гравити Фолз')
        collector.set_book_genre('Оно','Ужасы')
        collector.set_book_genre('Гравити Фолз','Мультфильмы')
        assert collector.get_books_for_children() == ['Гравити Фолз']

    def test_add_book_in_favorites_adds_book(self,collector):
        collector.add_new_book('Собака Баскервилей')
        collector.set_book_genre('Собака Баскервилей','Детективы')
        collector.add_book_in_favorites('Собака Баскервилей')
        assert collector.get_list_of_favorites_books() == ['Собака Баскервилей']

    def test_delete_book_from_favorites_removes_book(self,collector):
        collector.add_new_book('Собака Баскервилей')
        collector.set_book_genre('Собака Баскервилей','Детективы')
        collector.add_book_in_favorites('Собака Баскервилей')
        collector.delete_book_from_favorites('Собака Баскервилей')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_returns_list(self,collector):
        collector.add_new_book('Собака Баскервилей')
        collector.add_book_in_favorites('Собака Баскервилей')
        assert collector.get_list_of_favorites_books() == ['Собака Баскервилей']



