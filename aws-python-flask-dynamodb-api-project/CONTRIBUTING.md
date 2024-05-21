# 開発者向けのドキュメント

## アプリケーションをデプロイ

```
$ docker-compose run --rm -v "$PWD"/aws-python-flask-dynamodb-api-project:/app sls-cli sh -c "npx serverless deploy"
$
```

## ローカル環境に WebAPI をコールする方法

### 画像情報を保存

```
$ echo '{"name": "dog_1", "image": "'$(base64 -w0 ./tests/data/100x100_red.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images
$ echo '{"name": "dog_2", "image": "'$(base64 -w0 ./tests/data/100x100_blue.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images
$ echo '{"name": "dog_3", "image": "'$(base64 -w0 ./tests/data/100x100_green.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images
$ echo '{"name": "dog_4", "image": "'$(base64 -w0 ./tests/data/100x100_yellow.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images
$ echo '{"name": "dog_5", "image": "'$(base64 -w0 ./tests/data/100x100_orange.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images
$
```

### 開発環境に画像情報を保存

```
$ echo '{"name": "dog_1", "image": "'$(base64 -w0 ./tests/data/100x100_red.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
$ echo '{"name": "dog_2", "image": "'$(base64 -w0 ./tests/data/100x100_blue.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
$ echo '{"name": "dog_3", "image": "'$(base64 -w0 ./tests/data/100x100_green.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
$ echo '{"name": "dog_4", "image": "'$(base64 -w0 ./tests/data/100x100_yellow.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
$ echo '{"name": "dog_5", "image": "'$(base64 -w0 ./tests/data/100x100_orange.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
```

### 犬画像を保存

```
$ echo '{"name": "sleeping dog", "image": "'$(base64 -w0 21445_390x390.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
$ echo '{"name": "dog looking at camera", "image": "'$(base64 -w0 21446_390x390.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/images
$
```

## 保存した画像をランダム

curl https://bsqx5trty6.execute-api.ap-northeast-1.amazonaws.com/random_image

### 詳細な画像情報を取得する

画像 ID を指定し、詳細な画像データを取得します。

```
$ curl http://0.0.0.0:5000/images/1
$
```

### ランダムな画像情報を取得

```
$ curl http://0.0.0.0:5000/random_image
$
```

## aws cli でデータを参照

```
$ aws dynamodb list-tables --endpoint-url http://localhost:8000
$ aws dynamodb scan --table-name images-table-dev --endpoint-url http://localhost:8000
$
```
