def handler(request):
    query = request.body.decode('utf-8').replace('+', ' ')
    return {
        'statusCode': 302,
        'headers': {
            'Location': f'https://www.google.com/search?q={query}'
        }
    }
