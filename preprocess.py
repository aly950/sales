import numpy as np
def item_fat(fat):
    return 0 if fat.lower().strip()=='low fat' else 1

def product_type(product):
    if product.lower().strip()=='baiking goods':
        return 0
    if product.lower().strip()=='breads':
        return 1
    if product.lower().strip()=='breakfast':
        return 2
    if product.lower().strip()=='canned':
        return 3
    if product.lower().strip()=='Dairy':
        return 4
    if product.lower().strip()=='frozen food':
        return 5
    if product.lower().strip()=='fruits and vegetables':
        return 6
    if product.lower().strip()=='hard drinks':
        return 7
    if product.lower().strip()=='health and hygiene':
        return 8
    if product.lower().strip()=='household':
        return 9
    if product.lower().strip()=='meat':
        return 10
    if product.lower().strip()=='others':
        return 11
    if product.lower().strip()=='seafood':
        return 12
    if product.lower().strip()=='snak Foods':
        return 13
    if product.lower().strip()=='soft drinks':
        return 14
    if product.lower().strip()=='starchy foods':
        return 15


def size(size):
    if size.lower().strip()=='small':
        return 2
    if size.lower().strip()=='medium':
        return 1
    else:
        return 0

def population(population):
    if population.lower().strip()=='tier 1':
        return 0
    if population.lower().strip()=='tier 2':
        return 1
    else:
        return 2

def market_type(market):
    if market.lower().strip()=='supermarket type1':
        return 1
    if market.lower().strip()=='supermarket type2':
        return 2
    if market.lower().strip()=='supermarket type3':
        return 3
    else:
        return 0

def preprocess_data(data):
    Item_Weight = data['weight']
    
    Item_Fat_Content=item_fat(data['fat'])
    
    Item_Type=product_type(data['product'])
    
    Item_MRP=data['price']
    
    Outlet_Size =size(data['size'])
    
    Outlet_Location_Type= population(data['population'])
    
    Outlet_Type=market_type(data['market'])
    
    final_data = [[Item_Weight,Item_MRP,Item_Fat_Content,Item_Type,Outlet_Size,Outlet_Location_Type,Outlet_Type]]
    
    return (final_data)
