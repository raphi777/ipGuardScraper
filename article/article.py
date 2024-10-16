class Article:
    def __init__(self, title, description, price, seller, published_at, marketplace, url, image_url, search_term):
        self.title = title
        self.description = description
        self.price = price
        self.seller = seller
        self.published_at = published_at
        self.marketplace = marketplace
        self.url = url
        self.image_url = image_url
        self.search_term = search_term

    def print_props(self):
        print("PRINTING PROPS:")
        print(self.title)
        print(self.description)
        print(self.price)
        print(self.seller)
        # print(self.published_at)
        print(self.marketplace.id)
        print(self.url)
        print(self.image_url)
        print(self.search_term)
        print("\n")
