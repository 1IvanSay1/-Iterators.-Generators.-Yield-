import types

def flat_generator(list_of_lists):
    list = 0
    while list < len(list_of_lists):
        list1 = 0     
        while list1 < len(list_of_lists[list]):   
            yield list_of_lists[list][list1]
            list1 += 1
        list += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    return isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    print(test_2())