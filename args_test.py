def sample_func(name, age):
    print name
    print age


from requests import request


# sample_func(name='vithulan', age='25')

def get_new_app_secret():
    try:
        url = "https://dev-pulse.leapset.com:8080/getAppSecret"
        headers = {'app-id': 'pulse-agent', 'device-id': 1272}
        response = request(method='post', url=url, headers=headers, timeout=5)
        app_secret = response.headers.get('app-secret')
        status_code = response.status_code
        print app_secret
        print status_code
    except Exception as e:
        print e


# get_new_app_secret()

