from auth.signed_request import Client


class Order(object):
    def __init__(self, store_key):
        self.store_key = store_key

    def create(self, values):
        data = {"orders": values}
        res = Client.send(
            "POST", "/api/stores/{}/orders".format(self.store_key), None, data)
        return res.json()

    def update_recipient(self, external_order_id, recipient_data):
        data = {"recipient": recipient_data}
        res = Client.send(
            "PUT", "/api/stores/{}/orders/{}/recipient".format(
                self.store_key, external_order_id), None, data
        )
        return res.json()

    def update_status(self, external_order_id, new_status):
        data = {"order": {"order_status": new_status}}
        res = Client.send(
            "PUT", "/api/stores/{}/orders/{}/status".format(
                self.store_key, external_order_id), None, data
        )
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

    @classmethod
    def find(cls, id):
        res = Client.send("GET", "/api/orders/{}".format(id))
        return res.json()

    @classmethod
    def find_all(cls, params=None):
        res = Client.send("GET", "/api/orders", params)
        return res.json()
