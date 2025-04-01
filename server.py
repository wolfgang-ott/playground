from flask import Flask, request
from datetime import datetime
import logging
 
# Configure logging
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
 
app = Flask(__name__)
 
@app.before_request
def log_request_info():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    method = request.method
    path = request.path
    ip = request.remote_addr
    logging.info(f"{ip} {method} {path}")
 
@app.route('/hello')
def hello():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info("Responding to /hello")
    return f'Hello world! {current_time}'
 
if __name__ == '__main__':
    logging.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=False)