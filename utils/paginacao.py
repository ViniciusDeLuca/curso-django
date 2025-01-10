import math

def cria_paginacao(
    intervalo_paginas,
    qt_paginas,
    pagina_atual
):
    metade_intervalo = math.ceil(qt_paginas/2)
    comeco_intervalo = pagina_atual - metade_intervalo
    final_intervalo = pagina_atual + metade_intervalo

    comeco_intervalo_offset = abs(comeco_intervalo) if comeco_intervalo < 0 else 0
    
    if comeco_intervalo < 0:
        comeco_intervalo = 0
        final_intervalo += comeco_intervalo_offset
    
    return intervalo_paginas[comeco_intervalo:final_intervalo]