import click
import requests

@click.command()
@click.argument('initial')
@click.option('--method', default='GET', help='the http method to use')
def get_urls(initial: str, method: str):
    res = requests.request(method, initial)
    for r in res.history:
        print(r.url)
    print(res.url)

if __name__ == '__main__':
    get_urls()