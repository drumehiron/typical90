class Table():

    def __init__(self, H, W):
        """Table

        Args:
            H (int): Number of Rows
            W (int): Number of Columns
        """
        self.H = H
        self.W = W
        self.table = [[0] * W for _ in range(H)]

    def input(self):
        for h in range(H):
            self.table[h] = [int(x) for x in input().split()]

    def get_item(self,h,w):
        return self.table[h][w]

    def sum_rows(self):
        res = [0 for w in range(self.H)]
        for h in range(self.H):
            for w in range(self.W):
                res[h] += self.get_item(h,w)
        return res

    def sum_columns(self):
        res = [0 for w in range(self.W)]
        for h in range(self.H):
            for w in range(self.W):
                res[w] += self.get_item(h,w)
        return res

    def calc(self):
        import copy
        res = copy.deepcopy(self.table)
        sum_row = self.sum_rows()
        sum_columns = self.sum_columns()
        for w in range(self.W):
            for h in range(self.H):
                res[h][w] = 0
                res[h][w] = sum_columns[w] + sum_row[h] - self.get_item(h,w)
        return res

    def result(self):
        res = self.calc()
        for h in range(self.H):
            print(*res[h])

H, W = [int(x) for x in input().split()]

table = Table(H,W)

table.input()

result = table.result()
