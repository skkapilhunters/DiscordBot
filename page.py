from quart import Quart, jsonify

app = Quart(__name__)

@app.route('/')
async def home():
    """Health check / keep-alive endpoint for hosters like Render or Replit."""
    return jsonify({"status": "online", "message": "Bot web server is running."})

@app.route('/health')
async def health():
    return jsonify({"status": "ok"}), 200
