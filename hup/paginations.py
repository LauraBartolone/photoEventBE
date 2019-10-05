# -*- coding: utf-8 -*-
"""
    Pagination for DRF
"""
from __future__ import unicode_literals

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BasePagination(PageNumberPagination):
    """
        Base Pagination
    """

    page_size = 18
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):

        count_item = int(self.page.paginator.count)

        next_page = self.get_next_link()
        if next_page is not None:
            next_page = int(next_page)

        previous_page = self.get_previous_link()
        if previous_page is not None:
            previous_page = int(previous_page)

        return Response({'count': count_item,
                         'next': next_page,
                         'previous': previous_page,
                         'results': data})

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return str(page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return str(page_number)
