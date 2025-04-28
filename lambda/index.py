import json
import urllib.request

API_URL = "https://bd8b-35-194-179-239.ngrok-free.app/predict"  # ← あなたの今のngrok URL + /predict

def lambda_handler(event, context):
    body = json.loads(event['body'])
    user_message = body.get('message', '')

    # APIにPOSTするデータを作成
    request_data = json.dumps({"message": user_message}).encode('utf-8')
    
    # リクエスト作成
    req = urllib.request.Request(
        API_URL,
        data=request_data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )

    # API呼び出し
    with urllib.request.urlopen(req) as response:
        response_body = response.read()
        result = json.loads(response_body)

    # Lambdaのレスポンスとして返す
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'response': result['response']})
    }
