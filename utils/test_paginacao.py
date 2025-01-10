from unittest import TestCase
from utils.paginacao import cria_paginacao

class PaginacaoTest(TestCase):
    def test_cria_intervalo_paginacao_retorna_intervalo(self):
        paginacao = cria_paginacao(
            intervalo_paginas=list(range(1,21)),
            qt_paginas=4,
            pagina_atual=1
        )
        self.assertEqual([1,2,3,4], paginacao)        
        
        paginacao = cria_paginacao(
            intervalo_paginas=list(range(1,21)),
            qt_paginas=4,
            pagina_atual=2
        )
        self.assertEqual([1,2,3,4], paginacao)
        
        paginacao = cria_paginacao(
            intervalo_paginas=list(range(1,21)),
            qt_paginas=4,
            pagina_atual=3
        )
        
        self.assertEqual([2,3,4,5], paginacao)