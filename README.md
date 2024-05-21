# api-rdi-project

ランダムに犬画像を提供する WebAPI（random-dog-images）です。

# 提供するサービス

## GET / random_image

JSON 形式でランダムな犬の画像を取得することができます。

```
{
    'id': string, # ランダムな ID
    'name': string, # 犬の名前
    'image': string # base64 でエンコードされた犬の画像
}
```

curl でコールした例

```
$ curl https://xxxxxxxxxx.execute-api.amazonaws.com/random_image
{
    "id":"xxd7014d0a124ec6bb5025b1215be427",
    "image":"iVBORw0KGgoAAAANSUhEUgAAA...."
    "name":"dog looking at camera"
}
$
```

# 開発環境

- 開発ツール
  - serverless framework
  - Docker
- 言語
  - Python 3.8
- Web フレームワーク
  - Flask: 1.1.4
- 実行環境
  - AWS
    - Amazon API Gateway
    - Amazon DynamoDB
    - AWS Lambda
