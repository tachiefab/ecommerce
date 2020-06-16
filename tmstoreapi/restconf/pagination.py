from rest_framework import pagination



# class TMStoreAPIPagination(pagination.LimitOffsetPagination):
	
#     default_limit   = 10
#     max_limit       = 20


class TMStoreAPIPagination(pagination.PageNumberPagination):
	
   page_size   =  100

