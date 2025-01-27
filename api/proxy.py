import requests

def handler(request):
    url = request.query.get('url')

    if not url:
        return {'message': "Missing 'url' parameter"}, 400

    try:
        response = requests.get(url)
        return {
            'statusCode': response.status_code,
            'body': response.text,
            'headers': {
                'Content-Type': response.headers.get('Content-Type', 'text/html')
            }
        }
    except Exception as e:
        return {'message': str(e)}, 500
