from flask import Flask, jsonify, request
import psutil
import os

app = Flask(__name__)

@app.route('/div', methods=['POST'])
def divide():
    data = request.get_json()
    operand1 = data.get('operand1', 0)
    operand2 = data.get('operand2', 1)

    if operand2 == 0:
        return jsonify({'error': '零不能为除数！'})

    result = operand1 / operand2
    print(u'内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5003, debug=True)
