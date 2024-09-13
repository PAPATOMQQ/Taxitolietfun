from flask import Flask, request, jsonify

app = Flask(__name__)

# 模擬的數據庫
rides = []

# 添加共乘信息的路由
@app.route('/add_ride', methods=['POST'])
def add_ride():
    ride = request.get_json()
    rides.append(ride)
    return jsonify({'message': '共乘信息已添加', 'ride': ride}), 201

# 獲取所有共乘信息的路由
@app.route('/rides', methods=['GET'])
def get_rides():
    return jsonify({'rides': rides})

if __name__ == '__main__':
    app.run(debug=True)
