from auth.signed_request import Client


class Order(object):
    def __init__(self, store_key):
        self.store_key = store_key

    def create(self):
        pass

    def update_recipient(self):
        pass

    def update_status(self):
        pass

    @classmethod
    def find(cls, id):
        res = Client.send("GET", "/api/orders/{}".format(id))
        return res.json()

    def find_by_store(self, external_store_id):
        res = Client.send(
            "GET", "/api/stores/{}/orders/{}".format(self.store_key,
                                                     external_store_id))
        return res.json()

    def find_by_all_store(self, params=None):
        res = Client.send("GET",
                          "/api/stores/{}/orders".format(self.store_key),
                          params)
        return res.json()
        pass

    @classmethod
    def find_all(cls, params=None):
        res = Client.send("GET", "/api/orders", params)
        return res.json()

