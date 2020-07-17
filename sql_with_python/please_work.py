import pyodbc


class NWProducts:
    def __init__(self):
        self.server = 'databases.spartaglobal.academy'  # 'localhost, 1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.connection_string = "DRIVER={SQL Server};"
        self.connection_string += f"SERVER={self.server};"
        self.connection_string += f"DATABASE={self.database};"
        self.connection_string += f"UID={self.username};"
        self.connection_string += f"PWD={self.password}"
        self.northwind = pyodbc.connect(self.connection_string)  # creating the connection
        self.cursor = self.northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_average_unit_price(self):
        records = self._sql_query("SELECT * FROM Products;")
        total_unit_price = 0
        count_unit_price = 0
        for row in records:
            total_unit_price += row.UnitPrice
            count_unit_price += 1
        return total_unit_price / count_unit_price


# nw = NWProducts()
# print(nw.print_average_unit_price())

# TEST CLASS CODE WHEN IMPORTING:
if __name__ == "__main__":
    nw = NWProducts()
    print(nw.print_average_unit_price())

# # THIS WAS ALL DONE BEFORE NWProduct CLASS CREATED:
# cursor.execute("SELECT TOP 100 CompanyName, City FROM Customers WHERE Country = 'France';")
# row = cursor.fetchone()  # fetches top row
# print(row)
#
# rows = cursor.fetchall()  # don't want to use fetchall() with big databases
# print(rows)

# for row in cursor:
#     print(row)

# for row in cursor:  # better to fetch one row at a time as opposed to fetchall()
#     print(row[0])

# cursor.execute("SELECT * FROM Products;")

# for row in cursor:
#     print(row.UnitPrice)

# while True:
#     record = cursor.fetchone()
#     if record is None:
#         break
#     else:
#         print(type(record))
#         print(record.UnitPrice)

# cursor.execute("SELECT CategoryID, AVG(UnitPrice) as AvgPrice FROM Products GROUP BY CategoryID;")
#
# for row in cursor:
#     print(row.CategoryID, row.AvgPrice)

# # Write longer queries:
# query = """
#         SELECT CategoryID
#         , AVG(UnitPrice) AS AvgPrice
#         FROM Products
#         GROUP BY CategoryID;
#         """
# cursor.execute(query)

