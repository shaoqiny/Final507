import json, pandas as pd
from treelib import Tree

month_increase = pd.read_csv(r'final\processed_data\month_increase.csv')
month_increase['year'] = month_increase['year'].astype(str)
month_increase['monthly_increase'] = month_increase['monthly_increase'].astype(str)

def create_tree(df, items, parent, root=None, tree=None,  i=0):
    if tree is None:
        tree = Tree()
        root = root if root else parent
        tree.create_node(root, parent)

    i = i + 1

    for parental, group_df in df.groupby(items[i-1]):
        tree.create_node(parental[0], parental[1], parent=parent)
        if i <= len(items)-1: 
            create_tree(group_df, items, parental[1], tree=tree, i=i)
            
    return tree


month_tree = Tree()
items = [["year", "year"],
        ["month", "month"],
       ['monthly_increase', 'monthly_increase']]

tree = create_tree(month_increase.head(24), items, 'increase', 'Year' )

tree.show()

with open(r'final\tree\month_increase_tree.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(json.loads(tree.to_json()), ensure_ascii = False, indent = 1))

global_case = pd.read_csv(r'final\processed_data\global.csv', encoding = 'latin-1')
global_case['Cumulative_cases'] = global_case['Cumulative_cases'].astype(str)
items = [["WHO_region", "WHO_region"],
        ["Country", "Country"],
       ['Cumulative_cases', 'Cumulative_cases']]

tree2 = create_tree(global_case.head(228), items, 'increase', 'World' )
tree2.show()

with open(r'final\tree\global_case.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(json.loads(tree2.to_json()), ensure_ascii = False, indent = 1))