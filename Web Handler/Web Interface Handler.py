import requests as r

def main():
    url = 'http://192.168.1.1'
    credentials = {'usersname': 'username',
             'password': 'password'}
    post = r.post(url, data=credentials)
    print(post)

if '__main__' == __name__:
    main()
