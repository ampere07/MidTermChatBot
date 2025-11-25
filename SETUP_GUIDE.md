# Quick Setup Guide - Google Gemini 2.5 Flash Chatbot

## Using the Latest Gemini 2.5 Flash Model

Your chatbot now uses **gemini-2.5-flash** - the newest and fastest model from Google.

## Step-by-Step Instructions

### Step 1: Get Your Free Google Gemini API Key

1. Open your browser and go to: **https://aistudio.google.com/app/apikey**
2. Sign in with your Google account
3. Click the **"Create API Key"** button
4. Copy the generated API key (it will look like: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)

### Step 2: Update Your .env File

1. Open the `.env` file in your project folder
2. Replace the content with:
   ```
   GOOGLE_API_KEY=paste_your_actual_key_here
   ```
3. Save the file

### Step 3: Install/Update Dependencies

Open your terminal in the project folder and run:

```bash
# Activate virtual environment
venv\Scripts\activate

# Install/update packages
pip install --upgrade google-generativeai
pip install -r requirements.txt
```

### Step 4: Run Your Chatbot

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 5: Test in Browser

Open your browser and go to: **http://127.0.0.1:5000/**

## What Model Are We Using?

**gemini-2.5-flash** - The latest and fastest model from Google

### Benefits:
✓ **Latest technology** - Released in 2024
✓ **Fastest responses** - Optimized for speed
✓ **Free to use** - No credit card required
✓ **High quality** - Excellent AI responses
✓ **15 RPM limit** - Sufficient for testing and learning

## Available Models Comparison

| Model | Speed | Capability | Rate Limit (Free) |
|-------|-------|------------|-------------------|
| **gemini-2.5-flash** | ⚡⚡⚡ Fastest | High | 15 RPM, 1500 RPD |
| **gemini-2.5-pro** | ⚡⚡ Medium | Very High | 2 RPM, 50 RPD |
| **gemini-3-pro-preview** | ⚡ Slower | Highest | Limited access |

**RPM** = Requests Per Minute  
**RPD** = Requests Per Day

## Troubleshooting

### Error: "404 models/gemini-2.5-flash is not found"
```bash
pip install --upgrade google-generativeai
```

### Error: "No module named 'google.generativeai'"
```bash
pip install google-generativeai==0.8.3
```

### Error: "Invalid API key"
- Make sure you copied the entire key from Google AI Studio
- Check for extra spaces in the .env file
- Your key should start with "AIza"
- Get a new key from: https://aistudio.google.com/app/apikey

### Error: Port 5000 in use
Change the port in app.py:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

### Error: Rate limit exceeded
You have reached the free tier limit (15 requests per minute). Wait 60 seconds and try again.

## Testing Your Chatbot

Once running, try these test messages:
- "Hello, who are you?"
- "Explain artificial intelligence in simple terms"
- "Write a Python function to calculate factorial"
- "What is the difference between Flask and Django?"

## Model Selection (Advanced)

If you want to try different models, edit `app.py`:

```python
# For fastest responses (recommended)
model = genai.GenerativeModel('gemini-2.5-flash')

# For more complex reasoning
model = genai.GenerativeModel('gemini-2.5-pro')

# For experimental features
model = genai.GenerativeModel('gemini-3-pro-preview')
```

## Important Notes

- **gemini-2.5-flash** is the recommended model for chatbots due to speed
- Your API key is stored in `.env` and will not be committed to Git
- Free tier rate limits are sufficient for learning and testing
- Upgrade to paid tier only if deploying to production

## Next Steps

Once your chatbot is working:
1. Test different types of questions
2. Experiment with conversation flow
3. Customize the UI styling
4. Add conversation history feature
5. Try multimodal inputs (text + images with gemini-2.5-pro-vision)

## Need Help?

If you encounter issues:
1. Verify API key at https://aistudio.google.com/app/apikey
2. Check Python version: `python --version` (need 3.8+)
3. Ensure virtual environment is activated
4. Update packages: `pip install --upgrade google-generativeai`
5. Check Flask server logs for errors

Your chatbot is now using the latest Gemini 2.5 Flash model and ready for development!
