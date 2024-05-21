import os

import boto3
from flask import Flask, jsonify, make_response, request
from src.picture import Picture
from src.repository import Repository

app = Flask(__name__)


dynamodb_client = boto3.client('dynamodb')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', 
        region_name='dynamodb-local', 
        endpoint_url='http://dynamodb-local:8000'
    )

repository = Repository(dynamodb_client, os.environ['USERS_TABLE'])
picture = Picture(repository)

@app.route('/images/<string:id>')
def get_image(id):
    """画像情報を返す

    Args:
        id (str): 画像に紐付く ID

    Returns:
        dict: ID に紐付く詳細な画像情報を返す
    """
    image = picture.get_image(id)
    if not image.id:
        return jsonify({'error': 'Could not find user with provided id'}), 404

    return jsonify({
        'id': image.id, 
        'name': image.name,
        'image': image.image
    })


@app.route('/random_image')
def get_random_image():
    """ランダムに画像情報を返す

    Returns:
        dict: 画像情報を返す
    """
    image = picture.get_random_image()
    return jsonify({
        'id': image.id, 
        'name': image.name,
        'image': image.image
    })


@app.route('/images', methods=['POST'])
def create_image():
    """画像情報を作成

    Returns:
        _type_: _description_
    """
    name = request.json.get('name')
    image = request.json.get('image')
    if not name or not image:
        return jsonify({'error': 'Please provide both name and image'}), 400

    image = picture.create_image(name, image)
    return jsonify({
        'id': image.id, 
        'name': image.name
    })


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
