class Select:

    def __init__(self, columns):
        self.command = f"select {', '.join(columns)} "

    def where(self, column):
        self.command += f"where {column} "
        return self

    def and_where(self, column):
        self.command += f"and where {column} "
        return self

    def from_table(self, table):
        self.command += f"from {table} "
        return self

    def equals(self, str):
        self.command += f"= {str} "
        return self

    def lesser_than(self, str):
        self.command += f"< {str} "
        return self