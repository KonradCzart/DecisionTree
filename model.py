
class Node:
    def __init__(self, value):
        self.value = value
        self.child = {}

    def show_decision_tree(self, tree_level):
        if self.child:
            print("Atrybut: " + self.value)
            for key in self.child:
                for i in range(tree_level):
                    print('\t', end='')
                print(key + " -> ", end='')
                self.child[key].show_decision_tree(tree_level + 1)
        else:
            print("Decyzja: " + self.value)


class DecisionTable:

    def __init__(self):
        self.__table_list = []
        self.__row_size = 0

    def add_row(self, row):
        self.__table_list.append(row)
        self.__row_size += 1

    def get_attribute_size(self):
        return len(self.__table_list[0]) - 1

    def get_decision_class(self):
        decision_index = len(self.__table_list[0]) - 1
        return self.__table_list[0][decision_index]

    def calculate_parameter_usage(self, argument_index):
        result = {}
        for r in range(0, self.__row_size):
            key = self.__table_list[r][argument_index]
            value = result.get(key, 0)
            value += 1
            result[key] = value
        return result

    def calculate_decision_usage(self):
        decision_index = len(self.__table_list[0]) - 1
        return self.calculate_parameter_usage(decision_index)

    def divide_decision_table(self, attribute_index, attribute):
        table = DecisionTable()
        for r in range(0, self.__row_size):
            value = self.__table_list[r][attribute_index]
            if attribute == value:
                table.add_row(self.__table_list[r])
        return table

    def __str__(self):
        return str(self.__table_list)


