class Article:
    def __init__(self, title, brand, description, price, category, seller, published_at, marketplace, url, image_url,
                 search_term):
        self.title = title
        self.brand = brand
        self.description = description
        self.price = price
        self.category = category
        self.seller = seller
        self.published_at = published_at
        self.marketplace = marketplace
        self.url = url
        self.image_url = image_url
        self.search_term = search_term

    def print_props(self):
        print("PRINTING PROPS:")
        print(self.title)
        print(self.brand)
        print(self.description)
        print(self.price)
        print(self.category)
        print(self.seller)
        # print(self.published_at)
        print(self.marketplace)
        print(self.url)
        print(self.image_url)
        print(self.search_term)
        print("\n")
