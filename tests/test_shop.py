import unittest

from src.balatroish.shop import ShopOffer, ShopState


class ShopTests(unittest.TestCase):
    def test_buy_offer(self):
        shop = ShopState(
            offers=[
                ShopOffer(key="sigil_heart", title="Heart Ember", cost=4, description="+chips on Hearts")
            ]
        )
        remaining, offer = shop.buy("sigil_heart", money=7)
        self.assertEqual(remaining, 3)
        self.assertEqual(offer.title, "Heart Ember")
        self.assertEqual(len(shop.offers), 0)

    def test_buy_insufficient_funds(self):
        shop = ShopState(offers=[ShopOffer(key="x", title="X", cost=5, description="")])
        with self.assertRaises(ValueError):
            shop.buy("x", money=2)


if __name__ == "__main__":
    unittest.main()
