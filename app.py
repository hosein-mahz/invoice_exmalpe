user_invose = {
    "time" : 13,
    "user" : 1,
    "Price": 0,
    "order": [
        {
            "id": 1,
            "title":"kala1",
            "number":2
        },
        {
            "id": 2,
            "title":"kala2",
            "number":1
        }
    ]
}

warehouse =[
    {
        "id":1,
        "title":"kala1",
        "price":1500,
        "inventory":2
    },
    {
        "id" : 2,
        "title": "kala2",
        "price":2100,
        "inventory": 4
    },
    {
        "id" : 3,
        "title": "kala3",
        "price":1000,
        "inventory": 0
    }
]

def checkInvoice(orders, warehouse):
    x = []
    for order in orders:
        # print(x["title"])
        for y in warehouse:
            # print(y["title"])
            if order['title'] == y['title']:
                # print("kalay " + y['title'] + " dar anbar yafat shod")
                if order['number'] <= y["inventory"]:
                    # print ("kalay " + x["title"] + " be tedade " + str(y["inventory"]) + " ta dar anbar mojod ast")
                    x.append(order) 
    return x

def total_items(ssss,warehouse):
    total = 0
    for x in ssss:
        total = x['number'] + total
    return total

def total_price(price,warehouse):
    total = 0
    for x in price:
        # print(x["number"])
        for y in warehouse:
            # print(y["title"])
            if x["title"] == y["title"]:
                # print(y)
                total = ( x['number'] * y['price'] ) + total              
    return total                


total_price(user_invose["order"],warehouse)