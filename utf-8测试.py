import json;

transformed_body = "测试";
output = bytes(json.dumps(transformed_body).encode('UTF-8'));

print(output)