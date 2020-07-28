# 316493758
# 2

class Restaurant(object):
    """
    Restaurant class, do add, remove, reset and gives status of the restaurant
    """

    class Table(object):
        """
        Inner class of Table in the restaurant
        """

        def __init__(self, sits_count):
            """
            Constructor
            :param sits_count: sits count
            """
            self._sits_count = sits_count
            self._sits = {}

        def _group_in_table(self, group_name):
            """
            Get if group in the table
            :param group_name:
            :return:
            """
            return group_name in self._sits

        def _has_room(self, count):
            """
            Check if got room for amount of people
            :param count:   Number
            :return:        Boolean
            """
            return self.empty_sits_count() >= count

        def empty_sits_count(self):
            """
            Get count of empty sits
            :return: number
            """
            return self._sits_count - self.taken_sits_count()

        def taken_sits_count(self):
            """
            Get taken sits count
            :return: Number
            """
            return sum(self._sits.values())

        def add_group(self, group_name, group_count):
            """
            Add group to table
            :param group_name:  String
            :param group_count: Number
            :return:            Boolean
            """
            if self._has_room(group_count) and not self._group_in_table(group_name):
                self._sits[group_name] = group_count
                return True
            else:
                return False

        def remove_group(self, group_name):
            """
            Remove group from table
            :param group_name:  String
            :return:            Boolean
            """
            if self._group_in_table(group_name):
                del self._sits[group_name]
                return True
            else:
                return False

        def reset_table(self):
            """
            Reset Table
            :return:
            """
            self._sits = {}

        def print_table(self):
            print(self._sits_count, ": ", self._sits)

    def __init__(self, tables):
        """
        Constructor
        :param tables:  Array of numbers
        """
        self._tables = [Restaurant.Table(table) for table in tables]
        self._sit_order = {}

    def _find_best_table(self, group_count):
        """
        Find best table for group count,
        The best one is one that close the table.
        The worst one is one that left an empty sit.
        If there is no room return -1
        :param group_count: Number
        :return:            Table index
        """
        best_match = -1
        best_match_count = 0
        table_index = 0
        for index in range(len(self._tables)):
            empty_sits_count = self._tables[index].empty_sits_count()
            if empty_sits_count >= group_count:
                if empty_sits_count - group_count == 0:
                    return table_index
                else:
                    if best_match_count < 2:
                        best_match = table_index
                        best_match_count = empty_sits_count - group_count
            table_index += 1
        return best_match

    def group_seating(self, group):
        """
        Seating group
        :param group:   Tuple, first value is the group name
                        and the second is the people count
        :return:        Boolean
        """
        table_index = self._find_best_table(group[1])
        if table_index == -1 or group[0] in self._sit_order:
            return False
        else:
            self._sit_order[group[0]] = table_index
            self._tables[table_index].add_group(group[0], group[1])
        return True

    def group_removal(self, group_name):
        """
        Group removal
        :param group_name:  String
        :return:            Boolean
        """
        if group_name not in self._sit_order:
            return False
        else:
            self._tables[self._sit_order[group_name]].remove_group(group_name)
            del self._sit_order[group_name]
        return True

    def status(self):
        """
        Get people count in the restaurant
        :return:    Number
        """
        return sum([table.taken_sits_count() for table in self._tables])

    def reset(self):
        """
        Reset restaurant
        """
        for table in self._tables:
            table.reset_table()
        self._sit_order = {}

    def print_restaurant(self):
        """
        Print restaurant
        """
        for table in self._tables:
            table.print_table()
