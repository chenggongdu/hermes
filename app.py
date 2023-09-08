import uuid

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room

from base.common_class import MySocketIO, MyPineconeOP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
pinecone_op = MyPineconeOP()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_question', methods=['POST'])
def add_question():
    question = request.json.get('question')
    answer = request.json.get('answer')
    question_id = str(uuid.uuid4())
    texts = ['Q: {} A: {}'.format(question, answer)]
    ids = ["question_{}".format(question_id)]
    pinecone_op.insert(texts, ids)
    if not question or not answer:
        return jsonify({'error': '问题和答案不能为空'})

    return jsonify({'message': '常见问题已添加'})


@app.route('/del_question', methods=['POST'])
def del_question():
    ids = request.json.get('ids')
    if not ids:
        return jsonify({'error': 'ids不能为空'})
    pinecone_op.delete(ids)
    return jsonify({'message': '常见问题已删除'})


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    print(f'Client joined room: {room}')


@socketio.on('leave')
def handle_leave(data):
    if 'room' in data:
        room = data['room']
        leave_room(room)
        print(f'Client left room: {room}')
    else:
        print('Room not provided in data')


@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    room = request.sid  # 使用客户端的唯一标识符作为房间名
    llm = MySocketIO(socketio, room)
    llm.get_answer(message)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
