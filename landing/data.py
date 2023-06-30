from random import randint
import pandas as pd
headers = (
    "Name", "Errors", "Total Picks", "Picks Per Hour"
)
employee_header = (
    "Days Present","Role","Total Picks","Picks Per Hour","Errors","Leave"
)
contents = (
    ("Tobi Ghost", 1, 3589, 512),
    ("Edward Cole", 99, 358, 51),
    ("Roberts Carr", 1, 99900, 9999),
    ("Wade Williams", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Dave Harris", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Seth Thomas", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Ivan Robinson", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Riley Walker", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Gilbert Scott", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Jorge Nelson", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Dan Mitchell", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Brian Morgan", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Roberto Cooper", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Ramon Howard", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Miles Davis", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Liam Miller", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Nathaniel Martin", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Ethan Smith", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Lewis Anderson", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Milton White", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Claude Perry", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Joshua Clark", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Glen Richards", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Harvey Wheeler", randint(0, 5), randint(150, 3000), randint(120, 320)),
    ("Blake Warburton", randint(0, 5), randint(150, 3000), randint(120, 320))
)

def employeeOpen(name):
    df = pd.read_csv(f'landing\data\{name}.csv')
    return df

x = employeeOpen('Tobi Ghost')
employee_header = list(x.columns)
for rows_ in range(len(x.index)):
    # print(rows)
    for cols in range(len(employee_header)):
        # print(cols)
        # print(x.loc[rows,x.columns[cols]])
        pass
emp_dict = {}
table_list = []
def table_emp(table):
    tab = employeeOpen(table)
    employee_header = list(tab.columns)
    table_list = []
    for rows in range(len(tab.index)):
        emp_dict = {}
    #print(rows)
        for cols in range(len(employee_header)):
            emp_dict[employee_header[cols]] = tab.loc[rows,tab.columns[cols]]
            # print(employee_header[cols], ':', tab.loc[rows,tab.columns[cols]], end=' ')
        table_list.append(emp_dict)
    return table_list

# print(table_emp("Tobi Ghost")[0][employee_header[0]])
# row_s = table_emp("Tobi Ghost")[0]
# entries = row_s[employee_header[0]]
# 
# print(row_s)
# print(entries)        
