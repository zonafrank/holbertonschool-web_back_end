#!/usr/bin/env python3
"""Module for index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """When given page and pagesize as arguments Calculates the
      start and end index"""
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (page, end_index)