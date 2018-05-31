"""app.py"""
from flask import Flask, jsonify

APP = Flask(__name__)

#user requests with thier details
REQUESTS = [{'id':1, 'date':'2018-8-12', 'request':'Request1', 'status':'pending', 'user':'josh'},
            {'id':2, 'date':'2018-8-10', 'request':'Request2', 'status':'accepted', 'user':'mary'},
            {'id':3, 'date':'2018-8-9', 'request':'Request3', 'status':'resolved', 'user':'nakki'},
            {'id':4, 'date':'2018-8-1', 'request':'Request4', 'status':'rejected', 'user':'josh'}]

@APP.route('/api/v1/users/requests', methods=['GET'])
def get_all_requests():
    """ Returns all requests """
    return jsonify({'requests':REQUESTS, 'version':'1'})

if __name__ == '__main__':
    APP.run(debug=True)
    