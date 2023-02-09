import pytest 
from app import app
import json

def test_can_change():
    data = {"1": 1, "2": 2, "3": 3}
    response = app.test_client().get('/shuffle', json = data, content_type='application/json')
    res_data = response.data.decode('utf8').replace("'", '"')
    
    data_l = json.loads(res_data)
    response_json = json.dumps(data_l)
    assert response.status_code == 200
    assert response_json != json.dumps(data)
    
