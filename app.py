from flask import Flask, render_template, request, session, redirect, url_for
from textblob import TextBlob
import json

app = Flask(__name__)
app.secret_key = 'your-super-secret-key-for-sentiment-app'

def analyze_sentiment(text):
    """Returns sentiment label and polarity score (-1 to 1)"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive", polarity
    elif polarity < -0.1:
        return "negative", polarity
    else:
        return "neutral", polarity

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'notes' not in session:
        session['notes'] = []

    if request.method == 'POST':
        note_text = request.form.get('note', '').strip()
        if note_text:
            sentiment_label, polarity = analyze_sentiment(note_text)
            note_entry = {
                'text': note_text,
                'sentiment': sentiment_label,
                'polarity': round(polarity, 2)
            }
            session['notes'].append(note_entry)
            session.modified = True

    notes = session.get('notes', [])
    
    # Calculate stats
    total = len(notes)
    positive = len([n for n in notes if n['sentiment'] == 'positive'])
    negative = len([n for n in notes if n['sentiment'] == 'negative'])
    neutral = total - positive - negative

    return render_template('index.html',
                          notes=notes,
                          total=total,
                          positive=positive,
                          negative=negative,
                          neutral=neutral)

if __name__ == '__main__':
    app.run(debug=True)