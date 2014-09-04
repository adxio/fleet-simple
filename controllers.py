from flask import Blueprint, jsonify
from datatruck import Truck

car = Blueprint('mobil',__name__, url_prefix='/fleet/truck')

truk = Truck()
asli = truk.state()
jml = len(asli)

@car.route('/state')
def state():
    return jsonify(responses={'status_code':200,'message':'running'},output=asli)

@car.route('/position')
def position():
    data = {
        'status_code':200,
        'message':'OK'
    }
    for i in range(0,jml):
        jarak = asli[i]['distance']
        arah = asli[i]['head']
        vehicle_number = asli[i]['vehicle_number']
        if arah == 'L':
            if jarak == 0 and arah == 'L':
                distance = jarak + 1
                head = 'D'
            else:
                distance = jarak - 1
                head = 'L'
        else:
            if jarak == 10 and arah =='D':
                distance = jarak - 1
                head = 'L'
            else:
                distance = jarak + 1
                head = 'D'
        pros = {
            'distance':distance,
            'head':head,
            'vehicle_number':vehicle_number
        }
        asli[i] = pros
    return jsonify(responses=data,data=asli,vehicle=jml)

@car.route('/load')
def load():
    pulang = []
    for i in range(0,jml):
        jarak = asli[i]['distance']
        arah = asli[i]['head']
        vehicle_number = asli[i]['vehicle_number']
        if arah == 'L':
            pros = {
            'distance':jarak,
            'head':arah,
            'vehicle_number':vehicle_number
            }
            pulang.append(pros)
    res = {
        'status_code':200,
        'message':'OK'
    }
    return jsonify(response=res,data=pulang)

@car.route('/dump')
def dump():
    pulang = []
    for i in range(0,jml):
        jarak = asli[i]['distance']
        arah = asli[i]['head']
        vehicle_number = asli[i]['vehicle_number']
        if arah == 'D':
            pros = {
            'distance':jarak,
            'head':arah,
            'vehicle_number':vehicle_number
            }
            pulang.append(pros)
    res = {
        'status_code':200,
        'message':'OK'
    }
    return jsonify(response=res,data=pulang)

@car.route('/test')
def tes(env, start_response):
    start_response('200 OK', [('Content-Type','application/json')])
    return [b"Hello World"]