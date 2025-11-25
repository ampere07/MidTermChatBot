# AI Chatbot Project - Complete Documentation

## Project Overview
A fully working AI chatbot that uses Google Gemini 2.5 Flash API. The chatbot has a clean ChatGPT-style interface with typing animations, voice input/output, and theme switching.

## Features
- Real-time streaming responses (typing effect)
- Voice input (speech-to-text)
- Text-to-speech for AI responses
- Dark/Light theme switcher
- Clean, modern UI with smooth animations
- Copy to clipboard function
- Mobile responsive design

## Requirements
- Python 3.8 or higher
- Google Gemini API key (free)
- Modern web browser (Chrome, Edge, Firefox)

## Installation Steps

### 1. Get Google Gemini API Key
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key

### 2. Setup Project
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Add API Key
Open `.env` file and add your key:
```
GOOGLE_API_KEY=your_key_here
```

### 4. Run Application
```bash
python app.py
```

### 5. Open in Browser
Go to: http://127.0.0.1:5000/

## File Structure
```
MidTermChatBot/
├── app.py              # Backend server (Flask + Gemini API)
├── requirements.txt    # Python packages needed
├── .env               # API key (keep secret)
├── .gitignore         # Files to not upload to Git
├── README.md          # This file
└── static/
    └── index.html     # Frontend (HTML, CSS, JavaScript)
```

## How It Works

### Backend (app.py)
- Uses Flask to create a web server
- Connects to Google Gemini AI API
- Has two routes:
  - `/` - Serves the chat page
  - `/chat` - Handles messages and returns AI responses
- Supports streaming for typing effect

### Frontend (index.html)
- Clean ChatGPT-style interface
- Input starts centered, moves to bottom after first message
- Shows AI responses with typing animation
- Includes voice input and text-to-speech
- Theme switcher saves choice to browser

## Features Explained

### 1. Streaming Responses
- AI text appears word-by-word
- Shows blinking cursor while typing
- Natural conversation feel

### 2. Voice Input
- Click microphone icon
- Speak your message
- Automatically converts to text
- Red pulse animation when recording

### 3. Text-to-Speech
- Click "Speak" button on AI messages
- AI reads response aloud
- Uses browser's built-in voice

### 4. Theme Switcher
- Toggle between dark and light mode
- Saved to browser storage
- Smooth color transitions

### 5. Copy Function
- Click "Copy" to copy AI response
- Shows "Copied" confirmation
- Easy sharing of responses

## Code Quality

### Backend
- Clean imports at top
- Short, clear comments
- Functions do one thing
- Good error handling
- Modular structure

### Frontend
- Well organized CSS
- Clear variable names
- Commented sections
- Reusable functions
- Good event handling

## Testing Checklist

### Functionality
- [ ] Chat sends messages correctly
- [ ] AI responds without errors
- [ ] Streaming works smoothly
- [ ] Voice input works (Chrome/Edge)
- [ ] Text-to-speech works
- [ ] Copy button works
- [ ] Theme switcher saves choice

### UI/UX
- [ ] Welcome screen animates correctly
- [ ] Input moves to bottom smoothly
- [ ] Messages display clearly
- [ ] Buttons respond on hover
- [ ] Mobile layout works
- [ ] Colors are readable

### Integration
- [ ] Frontend connects to backend
- [ ] API key loads from .env
- [ ] Streaming data flows correctly
- [ ] Error messages show properly

## Common Issues

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "Invalid API key"
- Check .env file has correct key
- Make sure no extra spaces
- Get new key if needed

### Error: "Port 5000 in use"
```python
# Change port in app.py
app.run(debug=True, port=5001)
```

### Voice input not working
- Use Chrome or Edge browser
- Allow microphone permissions
- Check system microphone settings

## Browser Support
- Chrome: Full support
- Edge: Full support
- Firefox: Works (no voice input)
- Safari: Works (limited voice support)

## API Limits (Free Tier)
- 15 requests per minute
- 1500 requests per day
- More than enough for learning

## Future Ideas
- Save chat history
- Multiple chat sessions
- User accounts
- Custom AI settings
- Export conversations
- Mobile app version

## Security Notes
- Never share your API key
- .env file is in .gitignore
- No passwords in code
- Input is cleaned before sending
- Errors don't show sensitive info

## Credits
Created for AI integration coursework. Demonstrates:
- API integration
- Frontend/backend communication
- Modern web UI design
- Voice technology integration
- Responsive design principles

## Support
If you have problems:
1. Check API key is correct
2. Make sure virtual environment is active
3. Verify Python version (3.8+)
4. Check browser console for errors
5. Restart Flask server

## License
Free to use for learning and education purposes.
