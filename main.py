from configuration import ArgParser
from decision import Function
from model import DecisionTable


def read_array(config):
    table = DecisionTable()
    with open(config.get_input_path(), "r") as file:
        for row in file:
            split_row = row.strip().split(config.get_delimiter())
            table.add_row(split_row)
    return table


if __name__ == '__main__':
    conf = ArgParser.parse_argument()
    print(conf)
    decision_table = read_array(conf)
    node = Function.create_decision_tree(decision_table)
    node.show_decision_tree(1)

