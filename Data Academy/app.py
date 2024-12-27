from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Data penduduk sebagai contoh (ini bisa disimpan di database)
data_penduduk = {
    "1": {"nama": "Area 1", "jumlah_penduduk": 1000},
    "2": {"nama": "Area 2", "jumlah_penduduk": 1500},
}

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# API untuk mengambil data penduduk berdasarkan ID
@app.route('/api/data_penduduk', methods=['GET'])
def get_data_penduduk():
    area_id = request.args.get('id')
    if area_id in data_penduduk:
        return jsonify(data_penduduk[area_id])
    else:
        return jsonify({"error": "Data tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)
