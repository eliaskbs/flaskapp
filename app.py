import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page with a premium custom design."""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint for Azure App Service or monitoring tools."""
    return jsonify({
        "status": "healthy",
        "service": "flaskapp-azure",
        "version": "1.0.0"
    }), 200

if __name__ == '__main__':
    # Bind to PORT if defined by Azure environment, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
