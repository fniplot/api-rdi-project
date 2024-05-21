# 開発者向けのメモ

## npm プロジェクトを新規作成

```
$ docker-compose run --rm -v "$PWD":/app sls-cli sh -c "npm init -y"
$
```

## Serverless Framework 環境を構築

```
$ docker-compose run --rm -v "$PWD":/app sls-cli sh -c "npm install serverless"
$
```

## アプリケーションを作成

```
$ docker-compose run --rm -v "$PWD":/app sls-cli sh -c "npx serverless"
$ docker-compose run --rm -v "$PWD":/app sls-cli sh -c "npx serverless plugin install -n serverless-python-requirements"
$ docker-compose run --rm -v "$PWD":/app sls-cli sh -c "npx serverless plugin install -n serverless-dynamodb"
$
```

## DynamoDB を起動する方法（使用しない）

```
$ docker-compose run --rm -v "$PWD":/app -p 8000:8000 sls-cli sh -c "npx serverless dynamodb start"
$
```

## WSGI を起動する方法（使用しない）

```
$ docker-compose run --rm -v "$PWD":/app -p 5000:5000 sls-cli sh -c "npx serverless wsgi serve --host 0.0.0.0"
$
```

## コンテナにログイン

```
$ docker run --rm -it -v "$PWD":/app sls-cli /bin/bash
$
```

起動中のコンテナに接続する方法

```
$ docker exec -it 【container id】 /bin/bash
$
```

## 利用したサービス

### 画像を生成する Web サービス

- https://placehold.jp/
