#!/usr/bin/env python3
"""
Main file
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    This function calculates the start and end index for a given page and page size.

    Args:
        page: The current page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start and end index for the requested page.
    """

    if page < 1 or page_size <= 0:
        raise ValueError("Invalid page or page_size")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"


    def __init__(self):
        self.__dataset = None


    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data from the baby names dataset.

        Args:
            page: The page number (default: 1).
            page_size: The number of items per page (default: 10).

        Returns:
            A list containing the requested page of data, or an empty list if
            the page is out of range.
        """

        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        total_records = len(self.dataset())
        total_pages = math.ceil(total_records / page_size)  # Calculate total pages

        # Handle out-of-range pages
        if page > total_pages:
            return []

        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]


    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Provides hypermedia links for pagination.

        Args:
            page: The page number (default: 1).
            page_size: The number of items per page (default: 10).

        Returns:
            A dictionary containing hypermedia links for pagination.
        """

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
