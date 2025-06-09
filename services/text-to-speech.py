from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import os
import time

app = Flask(__name__)

SAVE_FOLDER = os.path.join(os.getcwd(), "audio_files")
os.makedirs(SAVE_FOLDER, exist_ok=True)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text')
    filename = data.get('filename', 'speech.mp3')

    if not text:
        return jsonify({"error": "Text is required"}), 400

    output_path = os.path.join(SAVE_FOLDER, filename)

    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    time.sleep(0.3)  # Ensure file is ready

    if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
        return jsonify({"error": "Audio file not created properly"}), 500

    return send_file(
        output_path,
        mimetype="audio/mpeg",
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
