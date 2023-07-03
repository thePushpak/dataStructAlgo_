'''
:created on: 4th July 2022
:author: Krishna choudhary
:email: krishna-dhinesh.choudhry@capgemini.com
:summary: This is a ML service for detecting objects as obstacles in Mining use case. This service takes a binary image as input and outputs centroids with labels of the detected Objects.
'''
import os
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pathlib import Path
import numpy as np

# np.random.BitGenerator = np.random.bit_generator.BitGenerator
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]

weights= str(ROOT/'best.pt')  # model.pt path(s)

data= str(ROOT/'classes.yaml')  # dataset.yaml path

# Get environment variables
try:
    device = os.environ.get('device', 'cpu')               # cuda device, i.e. 0 or 0,1,2,3 or cpu
except Exception as e:
    device = os.environ.get('DEVICE', 'cpu')
device = str(device)

try:
    PORT = os.environ.get('retail_service_port', 8081)
except Exception as e:
    PORT = os.environ.get('RETAIL_SERVICE_PORT', 8081)
PORT = int(PORT)

try:
    ALLOWED_IMG_TYPE = os.environ.get('allowed_img_type', ['jpg', 'png', 'jpeg'])
except Exception as e:
    ALLOWED_IMG_TYPE = os.environ.get('ALLOWED_IMG_TYPE', ['jpg', 'png', 'jpeg'])
ALLOWED_IMG_TYPE = list(ALLOWED_IMG_TYPE)

try:
    CONF_THRESH = os.environ.get('conf_thres', 0.8)
except Exception as e:
    CONF_THRESH = os.environ.get('conf_thres', 0.8)
CONF_THRESH = int(CONF_THRESH)

try:
    IOU_THRESH = os.environ.get('iou_thres', 0.5)
except Exception as e:
    IOU_THRESH = os.environ.get('iou_thres', 0.5)
IOU_THRESH = int(IOU_THRESH)

# instantiate app
def create_app(testing : bool = True):
    from pred import Init
    obj = Init(device, weights, data)
    app = Flask(__name__)

    # Enable CORS
    cors = CORS(app, resources={r'/*': {'origins': '*'}})
    app.config['CORS_HEADERS'] = 'Content-Type'


    @app.route('/', methods=['GET'])
    def service_info():
        try:
            result = {
                'version':'1.1',
                'ServiceName':'Vehicle model type Inference Service',
                'ServiceDescription': 'This is a ML service for detecting vehicle model type use case. This service takes a binary image as input and outputs centroids with labels of the detected Objects.',
            }
            return jsonify({'result': result}), 200
        except Exception as e:
            print('EXCEPTION: ', str(e))
            return jsonify({'result': str(e)}), 500

    @app.route('/infer', methods=['POST'])
    def predict_image_handler():
        try:
            req1 = None
            if ('imageData' in request.files):
                req1 = request.files['imageData']
            elif ('imageData' in request.form):
                req1 = request.form['imageData']
            else:
                req1 = request.get_data()
            images = []
            image = np.frombuffer(req1, np.uint8)
            images.append(image)
            # print("hello")
            rec_list = obj.pred(images,conf_thres=CONF_THRESH,iou_thres=IOU_THRESH)
            return make_response(jsonify(result = rec_list), 200)

        except Exception as e:
            print('EXCEPTION1:', str(e))
            return jsonify({'result': str(e)}), 400
    return app

if __name__ == '__main__':
    from pred import Init
    obj = Init(device, weights, data)
    app=create_app()

    create_app().run(host='0.0.0.0', port=PORT, debug=False, threaded=True)