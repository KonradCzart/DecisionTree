import math
from model import Node

class Function:

    @staticmethod
    def calculate_entropy(attribute_values):
        values = attribute_values.values()
        value = sum(values)
        entropy = 0
        for single_value in values:
            probability = single_value / value
            entropy += probability * math.log2(probability)
        return (-1)*entropy

    @staticmethod
    def calculate_info(table):
        decision_usage = table.calculate_decision_usage()
        return Function.calculate_entropy(decision_usage)

    @staticmethod
    def calculate_attribute_info(attribute_index, table):
        attribute_values = table.calculate_parameter_usage(attribute_index)
        set_power = sum(attribute_values.values())
        result = 0
        for attribute in attribute_values:
            divide_table = table.divide_decision_table(attribute_index, attribute)
            decision_usage = divide_table.calculate_decision_usage()
            result += (attribute_values[attribute]/set_power)*Function.calculate_entropy(decision_usage)
        return result

    @staticmethod
    def calculate_gain(table_info_value, attribute_info_value):
        return table_info_value - attribute_info_value

    @staticmethod
    def calculate_split_info(attribute_index, table):
        attribute_values = table.calculate_parameter_usage(attribute_index)
        return Function.calculate_entropy(attribute_values)

    @staticmethod
    def calculate_gain_ratio(gain_value, split_info_value):
        if gain_value == 0:
            return 0
        return gain_value/split_info_value

    @staticmethod
    def calculate_attribute_gain_ration(attribute_index, table, table_info_value):
        attribute_info_value = Function.calculate_attribute_info(attribute_index, table)
        attribute_gain_value = Function.calculate_gain(table_info_value, attribute_info_value)
        attribute_split_info_value = Function.calculate_split_info(attribute_index, table)
        return Function.calculate_gain_ratio(attribute_gain_value, attribute_split_info_value)

    @staticmethod
    def create_decision_tree(table):
        table_entropy_info = Function.calculate_info(table)
        max_gen_ratio_index = 0
        max_gen_ratio_value = 0
        for attribute_index in range(table.get_attribute_size()):
            gen_ratio = Function.calculate_attribute_gain_ration(attribute_index, table, table_entropy_info)
            if gen_ratio > max_gen_ratio_value:
                max_gen_ratio_value = gen_ratio
                max_gen_ratio_index = attribute_index

        if max_gen_ratio_value > 0:
            attribute_values = table.calculate_parameter_usage(max_gen_ratio_index)
            node = Node("a" + str(max_gen_ratio_index + 1))
            for attribute in attribute_values:
                divide_table = table.divide_decision_table(max_gen_ratio_index, attribute)
                node.child[attribute] = Function.create_decision_tree(divide_table)
            return node

        else:
            return Node(table.get_decision_class())


