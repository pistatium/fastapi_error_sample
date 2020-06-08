import json
from api.main import app

with open('openapi.json', 'w') as f:
    json.dump(app.openapi(), f)
