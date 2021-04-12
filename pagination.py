import itertools

str_in_lst = ['asdfghjklzxcvbnmqwerty']


class Pagination:

    def __init__(self, items: list, page_size: int = 10):  # Takes a list and count of items per page
        self.items = items
        self.page_size = page_size
        _separated_objects = list(''.join(self.items))  # Separating objects character by character
        _list_by_group = [_separated_objects[i:i + page_size] for i in range(0, len(_separated_objects), page_size)]
        # Above list comprehension, which takes a character-by-character separable list and creates "mini-lists"
        # of a certain number of items per page, the size itself is specified in (page_size in init)
        self.__book = dict(zip(itertools.count(1), _list_by_group))
        # Makes numbering of mini-lists (pages)
        self.used_page = 1  # Current page (counter)

    def get_visible_items(self):  # Shows what's on the current page (displays a specific mini-list)
        print(self.__book[self.used_page])
        return self  # Creates the ability to chain method calls

    def prev_page(self):  # Go to previous page with page out-of-range check
        if self.used_page > 1:
            self.used_page -= 1
        else:
            print('You are already on the first page.')
        return self

    def next_page(self):  # Move to next page with page out of range check
        if self.used_page < len(self.__book):
            self.used_page += 1
        else:
            print('The current page is the last, there is nowhere to turn.')
        return self

    def first_page(self):  # Go to start(first) page
        self.used_page = 1
        return self

    def last_page(self):  # Go to the last page
        self.used_page = len(self.__book)
        return self

    def go_to_page(self, number_page: int):  # Go to the specified page with a check for the existence of such a page
        if number_page != range(1, len(self.__book)):
            if number_page > len(self.__book):
                print(f'The specified page does not exist. '
                      f'Your page has been moved to the last one: {len(self.__book)}')
                return Pagination.last_page(self)
            elif number_page < 1:
                print(f'The specified page does not exist. Your page has been moved to the first one: {1}')
                return Pagination.first_page(self)
        else:
            self.used_page = number_page
        return self

    def get_current_page(self):  # Shows the current page number
        print(f'Current page: {self.used_page}')
        return self.used_page

    def get_page_size(self):  # Displaying the number of items on the current page
        print(f'Number of objects per page: {len(self.__book[Pagination.used_page])}')
        return len(self.__book[Pagination.used_page])

    def get_items(self):
        return self.items


if __name__ == "__main__":
    p = Pagination(str_in_lst, 4)
    
    p.get_visible_items()
    p.get_current_page()
    p.next_page()
    p.prev_page()
    p.last_page()
    p.first_page()
    p.get_page_size()
    p.get_current_page()
    p.get_items()
    p.go_to_page(11).prev_page().prev_page().next_page().get_visible_items()
