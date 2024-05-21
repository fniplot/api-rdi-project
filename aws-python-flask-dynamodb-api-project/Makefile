
local_setup:
	@echo '{"name": "dog_1", "image": "'$(shell base64 -w0 ./tests/data/100x100_red.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images;
	@echo '{"name": "dog_2", "image": "'$(shell base64 -w0 ./tests/data/100x100_blue.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images;
	@echo '{"name": "dog_3", "image": "'$(shell base64 -w0 ./tests/data/100x100_green.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images;
	@echo '{"name": "dog_4", "image": "'$(shell base64 -w0 ./tests/data/100x100_yellow.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images;
	@echo '{"name": "dog_5", "image": "'$(shell base64 -w0 ./tests/data/100x100_orange.png)'"}' | curl -X POST -H "Content-Type: application/json" -d @- http://0.0.0.0:5000/images 

info:
	docker-compose run --rm -v "$PWD"/aws-python-flask-dynamodb-api-project:/app sls-cli sh -c "npx serverless info"