!pip install TTS
import subprocess
from flask import Flask, request, jsonify
import base64
from TTS.api import TTS
app = Flask(__name__)
@app.route('/ask_desa', methods=['POST','GET'])
def ask_desa():
    data = request.json
    question = data.get('question')

    if not question:
        response_json = {
                "tipo": 'error',
                "response": 'ha ocurrido un error'  # Nueva propiedad agregada
                }
        return jsonify(response_json), 400
    print(question)
    try:
        tts=TTS("tts_models/multilingual/multi-dataset/xtts_v2")
        texto = "Una tormenta tropical es un fenómeno meteorológico que se caracteriza por fuertes vientos, lluvias intensas y turbulencia en el océano. Se forma sobre aguas cálidas en zonas tropicales y se caracteriza por una baja presión atmosférica. Estas tormentas pueden dar origen a huracanes si alcanzan vientos sostenidos de más de 119 km/h. Durante una tormenta tropical, pueden producirse inundaciones, deslizamientos de tierra y otros daños materiales significativos. Por lo tanto, es importante tomar medidas de prevención y seguir las instrucciones de las autoridades ante la llegada de una tormenta tropical."
        tts.tts_to_file(text=texto,speaker_wav='/content/drive/MyDrive/voz_sere.wav',language="es",file_path = "/content/voz_clonada_prueba_9.wav")
        tts.tts_to_file(text=texto, file_path="/content/voz_clonada_prueba_9.wav")
        def audio_to_base64(audio_path):
            with open(audio_path, 'rb') as audio_file:
                audio_data = audio_file.read()
                base64_audio = base64.b64encode(audio_data).decode('utf-8')
            return base64_audio
        response_text = audio_to_base64("/content/voz_clonada_prueba_9.wav")
        response_json = {
                "tipo": 'text',
                "response": response_text # Nueva propiedad agregada
                }
        return jsonify(response_json), 200
    except Exception as e:
        response_json = {
                "tipo": 'error',
                "response": 'ha ocurrido un error'  # Nueva propiedad agregada
                }
        return jsonify(response_json), 500
if __name__ == "__main__":
    app.run(port=47525)
