# qa_python
## Описание проекта

В данном проекте реализовано тестирование класса BooksCollector.

Цель работы — проверить корректность работы методов класса с помощью автоматических тестов на библиотеке pytest.

---

##  Используемые технологии

* Python
* pytest

---

##  Реализованные тесты

В проекте реализованы следующие проверки:

###  Добавление книг

* Проверка добавления двух новых книг:                                  
test_add_new_book_add_two_books

* Проверка, что одинаковые книги не добавляются повторно:               
test_add_new_book_not_add_double

* Проверка ограничений на длину названия книги (параметрический тест):  
test_add_new_book_invalid_name_not_added

###  Добавление в избранное

* Проверка добавления существуюшщей книги в список избранного:          
test_add_book_in_favorites_adds_book

* Проверка получения списка избранного:                                 
test_get_list_of_favorites_books_returns_list

###  Удаление из избранного

* Проверка удаления книги из избранного:                                
test_delete_book_from_favorites_removes_book

###  Добавление книге жанра:

* Проверка присвоения книге жанра:                                      
test_get_book_genre_adding_book_to_genre

* Проверка отсутствия жанра у добавленной книги:                        
test_set_book_genre_not_sets_genre

###  Фильтрация по жанру

* Проверка получения книг определённого жанра:                          
test_get_books_with_specific_genre_returns_books

* Проверка получения словаря books_genre:                               
test_get_books_genre_returns_dict

* Проверка возвращения пустого списка, когда жанр не существует: 
test_get_books_with_specific_genre_not_genre_empty_list

* Проверка возвращения пустого списка, когда жанр существует, но книг, соответствуюзего жанра нет:
test_get_books_with_specific_genre_not_book_empty_list

###  Возрастные ограничения

* Проверка, что книги с возрастным рейтингом не попадают в список для детей: 
test_get_books_for_children_returns_allowed_book
