
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'Hoodie', 'description': 'For Men', 'price': 44.99, 'url': 'https://images.footballfanatics.com/georgetown-hoyas/mens-champion-navy-georgetown-hoyas-team-arch-reverse-weave-pullover-hoodie_pi4266000_altimages_ff_4266580-8b5a060e842e7a7316b9alt1_full.jpg?_hv=2&w=900'},
    {'id': 2, 'name': 'Sweater', 'description': 'For Women', 'price': 39.99, 'url': 'https://images.footballfanatics.com/georgetown-hoyas/womens-cutter-and-buck-navy-georgetown-hoyas-lakemont-tri-blend-v-neck-pullover-sweater_pi5160000_altimages_ff_5160338-63dde443a49da303cb9dalt1_full.jpg?_hv=2&w=900'},
    {'id': 3, 'name': 'Accesories', 'description': 'Drinks Tumbler', 'price': 19.99, 'url': 'https://images.footballfanatics.com/georgetown-hoyas/georgetown-hoyas-18oz-stainless-steel-soft-touch-tumbler_pi4251000_ff_4251018-513e88aca198a4c5f3a2_full.jpg?_hv=2&w=900'},
   # {'id': 4, 'name': 'Online Course', 'description': 'Level up your programming skills.', 'price': 129.99, 'url': 'https://picsum.photos/id/180/360/200'},
    #{'id': 5, 'name': '________', 'description': '___________.', 'price': 0.99, 'url': '__________'},
    #{'id': 6, 'name': '________', 'description': '___________.', 'price': 0.99, 'url': '__________'},
]


class Product:
    def __init__(self, attrs):
        self.id = attrs.get("id")
        self.name = attrs.get("name")
        self.description = attrs.get("description")
        self.price = attrs.get("price")
        self.url = attrs.get("url")
        self.created_at = attrs.get("created_at")

    @property
    def to_row(self):
        return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]
