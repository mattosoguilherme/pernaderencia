from flask import Flask, request, jsonify, send_file
from flask_swagger_ui import get_swaggerui_blueprint
import os
import json
from automation import gerar_json_de_excel, executar_automacao
from flask_cors import CORS
import sys
sys.stdout.reconfigure(encoding='utf-8')




app = Flask(__name__)
CORS(app)

# ====== CONFIG SWAGGER ======
SWAGGER_URL = '/api'
API_URL = '/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Automação Pernaderencia"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route(API_URL)
def swagger_spec():
    """Serve o arquivo swagger.yaml"""
    return send_file('swagger.yaml')


@app.route('/')
def home():
    """Rota raiz: exibe status da API."""
    return jsonify({
        "status": "✅ API online",
        "documentacao": "/docs"
    })
    
@app.route('/upload-planilha', methods=['POST'])
def upload_planilha():
    """Recebe o upload da planilha Excel e gera o JSON."""
    try:
        if 'file' not in request.files:
            return jsonify({"erro": "Nenhum arquivo enviado."}), 400

        file = request.files['file']

        # Define diretórios absolutos
        base_dir = os.path.dirname(os.path.abspath(__file__))
        input_dir = os.path.join(base_dir, "input")
        os.makedirs(input_dir, exist_ok=True)

        # Caminhos absolutos
        caminho_excel = os.path.join(input_dir, file.filename)
        caminho_json = os.path.join(input_dir, "dados.json")

        # Salva o arquivo Excel
        file.save(caminho_excel)

        # Gera o JSON a partir da planilha
        gerar_json_de_excel(caminho_excel, caminho_json)

        # Verifica se o JSON foi realmente criado
        if not os.path.exists(caminho_json):
            return jsonify({"erro": f"Arquivo JSON não foi gerado em: {caminho_json}"}), 500

        return jsonify({
            "status": "JSON gerado com sucesso",
            "arquivo": caminho_json.replace("\\", "/")  # deixa o caminho legível no JSON
        }), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# ====== MAIN ======
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)