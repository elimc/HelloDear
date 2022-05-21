import json
import falcon
import dbm  # apparently python has a built-in key/value store already


class Store:
    def on_get(self, req, resp):
        with dbm.open("hellodear", "c") as db:
            config = {str(key, "utf-8"): str(db.get(key), "utf-8") for key in db.keys()}
            resp.text = json.dumps(config, ensure_ascii=False)
            resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        with dbm.open("hellodear", "c") as db:
            config = req.media
            db.update(config)
            resp.status = falcon.HTTP_200
