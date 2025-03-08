import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ai_core.assistant import AIAssistant
from interface.chat import ChatInterface
from database.jokes_db import JokesDatabase
from analytics.tracker import ActivityTracker

# Загрузка переменных окружения
load_dotenv()

app = Flask(__name__)
assistant = AIAssistant()
chat_interface = ChatInterface()
jokes_db = JokesDatabase()
activity_tracker = ActivityTracker()

@app.route('/')
def home():
    return render_template('base.html', title="Главная")

@app.route('/code-analysis', methods=['GET', 'POST'])
def code_analysis():
    if request.method == 'POST':
        code = request.form.get('code')
        analysis = assistant.analyze_code(code)
        return jsonify(analysis)
    return render_template('code_analysis.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chat/message', methods=['POST'])
def chat_message():
    message = request.json.get('message')
    response = chat_interface.process_text_message(message)
    return jsonify(response)

@app.route('/chat/voice', methods=['POST'])
def chat_voice():
    audio_data = request.files.get('audio').read()
    response = chat_interface.process_voice_message(audio_data)
    return jsonify(response)

@app.route('/jokes')
def jokes():
    return render_template('jokes.html', jokes=jokes_db.get_top_jokes())

@app.route('/stats')
def stats():
    stats_data = activity_tracker.get_productivity_stats()
    recommendations = activity_tracker.get_recommendations()
    return render_template('stats.html', stats=stats_data, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True) 