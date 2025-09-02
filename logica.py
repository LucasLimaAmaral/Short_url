import random, string, conexao_banco


def gera_link():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for i in range(6))

def encurta(mapp):
    url = mapp['url']
    
    shorturl = gera_link()
    return conexao_banco.post_url(url, shorturl)
