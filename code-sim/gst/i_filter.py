""" This is a modified version of the built-in filter function. It returns the
index of the first element for which function(element) is True"""


def index_filter(function, iterable):

    for index, element in enumerate(iterable):
        if function(element):
            yield index
