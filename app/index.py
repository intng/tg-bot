from flask import Flask, request, jsonify
from app.bot import reciever
import os
from app.api import regs
app = Flask(__name__)

@app.route('/tg/webhook/', methods=['POST'])
def tg_webhook():
    update = request.get_json()
    #try:

    if 'message' in update:
        if 'text' in update['message']:
            reciever.update(update)
    return jsonify({'success': True}), 200

@app.route('/api/activate/<token>')
def activate(token):
    return regs.activate(token)

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=int(os.getenv('flask_port')))