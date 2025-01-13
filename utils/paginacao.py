import math
from django.core.paginator import Paginator

def cria_intervalo_paginacao(
    intervalo_paginas,
    qt_paginas,
    pagina_atual
):
    metade_intervalo = math.ceil(qt_paginas/2)
    inicio_intervalo = pagina_atual - metade_intervalo
    final_intervalo = pagina_atual + metade_intervalo
    total_paginas = len(intervalo_paginas)

    inicio_intervalo_offset = abs(inicio_intervalo) if inicio_intervalo < 0 else 0
    
    if inicio_intervalo < 0:
        inicio_intervalo = 0
        final_intervalo += inicio_intervalo_offset
        
    if final_intervalo >= total_paginas:
        inicio_intervalo = inicio_intervalo - abs(total_paginas - final_intervalo)
        
    paginacao = intervalo_paginas[inicio_intervalo:final_intervalo]
    return {
        'paginacao': paginacao,
        'intervalo_paginas': intervalo_paginas,
        'qt_paginas': qt_paginas,
        'pagina_atual': pagina_atual,
        'total_paginas': total_paginas,
        'inicio_intervalo': inicio_intervalo,
        'final_intervalo': final_intervalo,
        'primeira_pagina_fora_do_intervalo': pagina_atual > metade_intervalo,
        'ultima_pagina_fora_do_intervalo': final_intervalo < total_paginas
    }

def cria_paginacao(request, queryset, num_registros):
    current_page = request.GET.get('page', 1)
    paginator = Paginator(queryset, num_registros)
    page_obj = paginator.get_page(current_page)
    
    intervalo_paginacao = cria_intervalo_paginacao(
        paginator.page_range,
        4,
        int(current_page)
    )
    
    return page_obj, intervalo_paginacao