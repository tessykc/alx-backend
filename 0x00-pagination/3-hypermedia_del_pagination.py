#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
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
        self.__indexed_dataset = None


    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset


    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Provides hypermedia links for pagination with deletion resilience.

        Args:
            index: The starting index of the requested page (default: None).
            page_size: The number of items per page (default: 10).

        Returns:
            A dictionary containing hypermedia links for pagination.
        """

        assert index is None or 0 <= index < len(self.indexed_dataset), "index out of range"

        indexed_dataset = self.indexed_dataset()
        total_records = len(indexed_dataset)

        # Handle initial request or request where index is out of range in the current dataset
        if index is None or index >= total_records:
            index = 0

        # Calculate next index based on page size, but don't go beyond total records
        next_index = min(index + page_size, total_records)

        # Return data slice based on the calculated indexes (handles deletions)
        data = [indexed_dataset[i] for i in range(index, next_index)]

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
