from Select import Select


class QueryBuilder:

    @staticmethod
    def select(columns):
        return Select(columns)
