class Matrix:
    def __init__(self, *rows):
        self.matrix = [row for row in rows]

    def __repr__(self):
        matrix_repr = ""
        for i, row in enumerate(self.matrix):
            row_repr = "   ".join(f"{n:6.2f}" for n in row[:-1])
            row_repr = f"{i}:   {row_repr}   | {row[-1]:6.2f}"
            matrix_repr += f"{row_repr} \n"
        return matrix_repr

    def scale(self, row, scalar):
        self.matrix[row] = [scalar * n for n in self.matrix[row]]

    def row_addition(self, source, destination, scalar=1):
        s = self.matrix[source]
        d = self.matrix[destination]
        self.matrix[destination] = [i + scalar * j for i, j in zip(d, s)]

    def swap(self, r1, r2):
        self.matrix[r1], self.matrix[r2] = self.matrix[r2], self.matrix[r1]
