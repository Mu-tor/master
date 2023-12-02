from flask import Flask, jsonify, request
import psutil
import os

app = Flask(__name__)

@app.route('/mul', methods=['POST'])
def multiply():
    data = request.get_json()
    operand1 = data.get('operand1', 1)
    operand2 = data.get('operand2', 1)
    result = operand1 * operand2
    print(u'内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
