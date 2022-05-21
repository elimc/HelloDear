import falcon
from api.config import Store

app = falcon.App(cors_enable=True)

config = Store()
app.add_route('/config', config)