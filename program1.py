from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [{
    'id':1,
    'Name':'Name',
    'Contact': 'Contact Numbver',
    'done':False,
}]

@app.route('/add-data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'Error',
            'message':'Please Provide the Data',
        },400)
    contact = {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }

    tasks.append(contact)
    return jsonify({
        'status':'success',
        'message':'Task Added Succesfully',
    })

@app.route('/get-data')

def get_task():
    return jsonify({
        'data':tasks
    })

if(__name__ == '__main__'):
    app.run(debug = True)
