
deploy:
	@docker-compose run --rm -v `pwd`/aws-python-flask-dynamodb-api-project:/app sls-cli sh -c "npx serverless deploy"

info:
	@docker-compose run --rm -v `pwd`/aws-python-flask-dynamodb-api-project:/app sls-cli sh -c "npx serverless info"
