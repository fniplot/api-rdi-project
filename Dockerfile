FROM node:20.11.1

# 最新の npm へアップグレート
RUN npm install -g npm@10.8.0

# serverless-dynamodb を実行するために必要
RUN apt-get update; apt-get install default-jre python3-pip -y

# python ライブラリをインストール
RUN pip3 install Werkzeug boto3 flask --break-system-package

# 作業ディレクトリを作成
WORKDIR /app
