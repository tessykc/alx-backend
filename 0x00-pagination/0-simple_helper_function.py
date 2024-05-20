#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
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

  # Handle potential errors
  if page < 1 or page_size <= 0:
    raise ValueError("Invalid page or page_size")

  # Calculate the start index based on page and page size
  start_index = (page - 1) * page_size

  # Calculate the end index, ensuring it doesn't exceed the total items
  end_index = start_index + page_size

  return start_index, end_index
