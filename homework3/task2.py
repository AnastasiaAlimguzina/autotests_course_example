def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    # todo Здесь нужно написать код
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average = round(sum_list/len(lst),2)
    my_tup = (min_elem, max_elem, sum_list, average)
    return my_tup
