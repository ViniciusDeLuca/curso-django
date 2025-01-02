import json
from faker import Faker
from random import randint

def rand_ratio():
    return randint(840, 900), randint(473, 573)

# Inicializa a instância do Faker
fake = Faker()

# Função para gerar uma entrada de receita fictícia
def gerar_receita_ficticia():
    return {
        'id' : fake.random_number(fix_len=True),
        'titulo': fake.sentence(nb_words=6),
        'descricao': fake.sentence(nb_words=12),
        'tempo_preparo': fake.random_number(digits=2, fix_len=True),
        'unidade_tempo_preparo': 'Minutos',
        'rendimento': fake.random_number(digits=2, fix_len=True),
        'unidade_rendimento': 'Porção',
        'etapas_preparo': fake.text(3000),
        'data_criacao': fake.date_time(),
        'autor': {
            'nome': fake.first_name(),
            'sobrenome': fake.last_name()
        },
        'categoria': {
            'nome': fake.word()
        },
        'capa': {
            'url': f'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

# # Gera múltiplas receitas fictícias
# def gerar_arquivo_receitas(nome_arquivo='receitas_ficticias.json', quantidade=18):
#     receitas_ficticias = [gerar_receita_ficticia() for _ in range(quantidade)]
#     # Salva as receitas geradas em um arquivo JSON
#     with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
#         json.dump(receitas_ficticias, arquivo, indent=4, ensure_ascii=False)
#     print(f"Arquivo '{nome_arquivo}' criado com {quantidade} receitas fictícias.")

# Gera o arquivo com o número desejado de receitas
if __name__ == "__main__":
    gerar_receita_ficticia()