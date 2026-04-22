#Mark Castillano Prelem
#BSIT 2-4    

def get_price_category(prince):
    if price < 50 :
        return "Budget"
    elif price < 199 :
        return "Mid-range"
    else:
        return "premium"
    
def check_stock_level(stock):
    if stock >= 10 :
        return "Ok"
    else:
        return "LOW-stock - reorder needed"
    
def save_product(name, price, category, stock, stock_status):
    with open('C:\\Castillano_Prelem\\product.txt', 'a') as file:
        file.write(f"product: {name} | Price : P{price:.2f} |  stock: {stock} | category: {category} | status: {stock_status} |\n")

while True:
    name = input("enter Product name: ")
    price = int(input("enter product price: "))
    stock = int(input("enter quantity in stock: "))

    category = get_price_category(price)
    status = check_stock_level(stock)

    print("price category: "+ category)
    print("stock status: "+ status)

    save_product(name, price, stock, category, status)
    print("product saved to inventory\n")

    choice = input("add another product? (yes or no): ").lower()
    if choice != "yes":
        print("inventory update complete. googbye!!")
        break