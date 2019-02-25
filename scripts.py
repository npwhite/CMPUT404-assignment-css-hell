import requests

def main():
    url = "http://www.gutenberg.org/files/74/74-h/images/spine.jpg"

    r = requests.get(url, allow_redirects=True)
    open('sawyer.jpg', 'wb').write(r.content)
    # print(r)



if __name__=="__main__":
    main()
