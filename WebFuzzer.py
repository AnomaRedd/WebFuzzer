# -*- coding: utf-8 -*-
""" 
WebFuzzer v0.1
__AUTHOR__:AnomaRed

This is a web fuzzer. Using this tool, you can find subdomain in web sites.
You can change the this code and add self projects.

"""
import requests
import click

@click.command()
@click.option("--url",help="--url example.com")
def main(url,port):
    subdom(url)

def subdom(url): #alt alan adı tarama
    print("""subdomain brute forcer is started\n
             ------------------------------------""")
    with open("sub-dom500 wordlist.txt","r") as f:
        i=0
        while i<500:
            word = str(f.readline())
            word = word[0:-1]
            link = "https://" + str(word) + "." + str(url)
            try:
                a = requests.get(link, allow_redirects=False)
            except:
                continue
            if a.status_code == 200:
                print("|" + str(a.status_code) + "| " + link + "[OK!]")
            elif a.status_code == 403:
                print("|" + str(a.status_code) + "| " + link + "[ACCESS DENIED]")
            elif a.status_code == 500:
                print("|" + str(a.status_code) + "| " + link + "[INTERNAL SERVER ERROR]")
            elif a.status_code == 502:
                print("|" + str(a.status_code) + "| " + link + "[BAD GATEWAY ERROR]")
            else:
                print("|" + str(a.status_code) + "| " + link)
            
        i+=1
    print("------------------------------------")
main()
