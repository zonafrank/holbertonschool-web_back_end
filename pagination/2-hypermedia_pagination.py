#!/usr/bin/env python3
"""Module for Server class and index_range function"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """When given page and pagesize as arguments Calculates the
      start and end index"""
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
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
        """Find the correct indexes to paginate the dataset correctly
        and return the appropriate data rows fromhe dataset
        """
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset()):
            return []
        return self.__dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """returns a dictionary containing the key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        Arguments:
        page(int): page number
        page_size(int): number of row per page
        """
        if self.__dataset is None:
            self.dataset()
        total_pages = math.ceil(len(self.__dataset) / page_size)
        data = self.get_page(page, page_size)

        next_page = page + 1
        if next_page > total_pages or next_page < 1:
            next_page = None

        prev_page = page - 1
        if prev_page < 1:
            prev_page = None

        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
