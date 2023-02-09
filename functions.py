import re
from typing import Iterable


def com_filter(data: Iterable[str], value: str) -> Iterable[str]:
    """
    The function takes as arguments the iterated sequence and the desired substring in the form of a string,
    implements the execution of the query in accordance with the "filter" command, searches for strings
    that include the desired substring. Returns the found elements in the original sequence as a list.
    """
    return filter(lambda x: value in x, data)


def com_map(data: Iterable[str], value: int) -> Iterable[str]:
    """
    The function takes as arguments the iterated sequence and the index of the string element as an integer,
    implements the execution of the query in accordance with the command "mar", selects the string elements
    having the required index. Returns the elements found in the original sequence as a list.
    """
    res = list()
    for line in data:
        for i, item in enumerate(line.split()):
            if i == value:
                res.append(item)
    return res


def com_unique(data: Iterable[str]) -> Iterable[str]:
    """
    The function takes an iterated sequence as an argument, implements the execution of the query in accordance
    with the "unique" command, selects unique elements of the original sequence. Returns the result as a list.
    """
    res = set(data)
    return list(res)


def com_limit(data: Iterable[str], value: int) -> Iterable[str]:
    """
    The function takes an iterated sequence and an integer parameter as arguments, implements the execution
    of the query in accordance with the "limit" command, selects the first elements of the original sequence
    in a specified number. Returns the result as a list.
    """
    res = list()
    for i, item in enumerate(data):
        if i < value:
            res.append(item)
    return res


def com_sort(data:Iterable[str], value: str) -> Iterable[str]:
    """
    The function takes as arguments an iterated sequence and a string parameter defining the sorting direction,
    implements the query execution in accordance with the "sort" command, sorts the elements of the original
    sequence in the specified direction. Returns the result as a list.
    """
    if value == "desc":
        return sorted(data, reverse=True)
    return sorted(data)


def com_regex(data: Iterable[str], value: str) -> Iterable[str]:
    """
    The function takes as arguments an iterable sequence and a string parameter, which is a template
    for searching for a substring, implements the execution of a query in accordance with the "regex" command,
    finds lines that include a substring. Returns the result as an iterable sequence.
    """
    pattern = re.compile(f'{value}')
    print(pattern)
    res = list()
    for line in data:
        if pattern.search(line):
            res.append(line)
    return res


#   Code for checking functionality and setting functions.
if __name__ == '__main__':

    print(com_regex(['1.181.2.178 [17/May/2015:20:05:36] "GET / HTTP/1.1" 200',
                    '1.125.2.148 [17/May/2015:20:05:19] "GET /?flav=rss20 HTTP/1.1" 200',
                    '1.170.2.204 [17/May/2015:20:05:03] "POST /?flav=atom HTTP/1.1" 200',
                    '1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200',
                    '1.163.30.77 [17/May/2015:20:05:37] "GET /blog/dot.html HTTP/1.1" 200'], 'images/\\w+\\.png'))