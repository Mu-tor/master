import asyncio
import psutil
import os

from flask import Flask, jsonify, request
import aiohttp
from flask_cors import CORS
app = Flask(__name__)
CORS(app)   # 启用 CORS 支持
async def call_multiply_service(operand1, operand2):
    url = "http://127.0.0.1:5002/mul"
    data = {'operand1': operand1, 'operand2': operand2}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            result = await response.json()
            return result.get('result', 0)

async def call_divide_service(operand1, operand2):
    url = "http://127.0.0.1:5003/div"
    data = {'operand1': operand1, 'operand2': operand2}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            result = await response.json()
            if 'error' in result:
                raise ValueError(result['error'])
            return result.get('result', 0)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    operand1 = data.get('operand1', 1)
    operand2 = data.get('operand2', 1)
    result = operand1 + operand2
    return jsonify({'result': result})

@app.route('/calculate', methods=['POST'])
async def calculate():
    data = request.get_json()
    operand1 = data.get('operand1', 1)
    operand2 = data.get('operand2', 1)

    try:
        # 异步调用乘法服务和除法服务
        mul_result, div_result = await asyncio.gather(
            call_multiply_service(operand1, operand2),
            call_divide_service(operand1, operand2)
        )

        # 计算加法结果
        result = mul_result + div_result

        print(u'内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
        return jsonify({'result': f"({operand1}×{operand2})+({operand1}÷{operand2})={result}"})

    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5001, debug=True)