from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AppDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)

def init_db():
    db.create_all()

@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    if not data or 'app_name' not in data or 'version' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    app_details = AppDetails(
        app_name=data['app_name'],
        version=data['version'],
        description=data.get('description', '')
    )
    db.session.add(app_details)
    db.session.commit()

    return jsonify({'message': 'App added successfully', 'app_id': app_details.id}), 201

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_details = AppDetails.query.get(id)
    if not app_details:
        return jsonify({'error': 'App not found'}), 404

    return jsonify({
        'id': app_details.id,
        'app_name': app_details.app_name,
        'version': app_details.version,
        'description': app_details.description
    })

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_details = AppDetails.query.get(id)
    if not app_details:
        return jsonify({'error': 'App not found'}), 404

    db.session.delete(app_details)
    db.session.commit()

    return jsonify({'message': 'App deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
