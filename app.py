"""
AI Chatbot Backend
Uses Google Gemini API for AI responses with streaming support
"""

from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai
import json
import time

# Load API key from .env file
load_dotenv()

# Setup Flask app
app = Flask(__name__, static_folder='static')
CORS(app)  # Allow frontend to talk to backend

# Setup Gemini AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/')
def index():
    """Serve the main chat page"""
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat messages from user
    Supports both streaming and regular responses
    """
    try:
        # Get user message from request
        data = request.get_json()
        user_message = data.get('message', '')
        stream = data.get('stream', False)
        
        # Check if message exists
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Streaming response (word by word)
        if stream:
            def generate():
                """Send AI response in chunks with delay for typing effect"""
                try:
                    response = model.generate_content(
                        user_message,
                        stream=True
                    )
                    # Send each chunk with small delay
                    for chunk in response:
                        if chunk.text:
                            # Split into smaller chunks for slower typing
                            text = chunk.text
                            for char in text:
                                yield f"data: {json.dumps({'text': char})}\n\n"
                                time.sleep(0.02)  # Delay between characters (adjust for speed)
                    # Tell frontend we're done
                    yield f"data: {json.dumps({'done': True})}\n\n"
                except Exception as e:
                    yield f"data: {json.dumps({'error': str(e)})}\n\n"
            
            # Return streaming response
            return Response(
                stream_with_context(generate()),
                mimetype='text/event-stream',
                headers={
                    'Cache-Control': 'no-cache',
                    'X-Accel-Buffering': 'no'
                }
            )
        
        # Regular response (all at once)
        else:
            response = model.generate_content(user_message)
            ai_response = response.text
            return jsonify({'response': ai_response})
        
    except Exception as e:
        # Return error if something goes wrong
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the server
    app.run(debug=True, host='127.0.0.1', port=5000)
