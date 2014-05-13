
__author__ = 'Sherlock'


class CPUMultiplier:

    def __init__(self):
        pass

    def multiply(self, matrix1, matrix2):

        row_num = self.get_row_length_of(matrix1)
        col_num = self.get_column_length_of(matrix2)
        result = [[0 for col in range(col_num)] for row in range(row_num)]

        for row in range(row_num):
            for col in range(col_num):
                result[row][col] = \
                    sum([matrix1[row][i]*matrix2[i][col]
                         for i in range(self.get_row_length_of(matrix2))])

        return result

    def get_row_length_of(self, matrix):
        return len(matrix[0])

    def get_column_length_of(self, matrix):
        return len(matrix)

