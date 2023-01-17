sheet_names = [
    'BASE MONETARIA', 
    'RESERVAS', 
    'DEPOSITOS', 
    'PRESTAMOS', 
    # 'TASAS DE MERCADO', 
    #'INSTRUMENTOS DEL BCRA',
    ]

cols_names = {
    'BASE MONETARIA': [
        'date',
        'delete_1',
        'VAR_DIARIA base monetaria',
        'VAR_DIARIA compra divisas sector privado',
        'VAR_DIARIA compra divisas al tesoro nacional',
        'VAR_DIARIA adelantos transitorios',
        'VAR_DIARIA transf utilidades',
        'VAR_DIARIA resto',
        'VAR_DIARIA pases',
        'VAR_DIARIA leliqs',
        'VAR_DIARIA redescuentos',
        'VAR_DIARIA intereses',
        'VAR_DIARIA lebacs',
        'VAR_DIARIA rescate cuasimonedas',
        'VAR_DIARIA otros',
        'delete_2',
        'VAR_DIARIA billetes publico',
        'VAR_DIARIA billetes entidades',
        'VAR_DIARIA cheques',
        'VAR_DIARIA cuenta corriente',
        'VAR_DIARIA semitotal',
        'VAR_DIARIA cuasimonedas',
        'VAR_DIARIA total',
        'delete_3',
        'billetes publico',
        'billetes entidades',
        'cheques',
        'cuenta corriente',
        'semitotal',
        'cuasimonedas',
        'total',
        'tipo_serie',
    ],
    'RESERVAS': [
        'date',
        'delete_1',
        'total',
        'oro divisas',
        'pase al exterior',
        'delete_2',
        'VAR_DIARIA reservas',
        'VAR_DIARIA compra divisas',
        'VAR_DIARIA oo ii',
        'VAR_DIARIA operaciones sector publico',
        'VAR_DIARIA efectivo minimo',
        'VAR_DIARIA otros',
        'delete_3',
        'asignaciones deg',
        'delete_4',
        'tipo de cambio',
        'tipo_serie',
    ],
    'DEPOSITOS': [
        'date', #1
        'TOTAL cc', #2
        'TOTAL ca', #3
        'TOTAL pf tradicional', #4
        'TOTAL pf uva', #5
        'TOTAL otros', #6
        'TOTAL cedros cer', #7
        'TOTAL total dep', #8
        'TOTAL boden', #9
        'TOTAL total', #10
        'PRIVADOS cc', #1
        'PRIVADOS ca', #2
        'PRIVADOS pf tradicional', #3
        'PRIVADOS pf uva', #4
        'PRIVADOS otros', #5
        'PRIVADOS cedros cer',#6 
        'PRIVADOS total dep', #7
        'PRIVADOS boden', #8
        'PRIVADOS total', #9
        'TOTAL depositos usd en ars', #10
        'PRIVADOS depositos usd en ars', #1
        'delete_1', #2
        'TOTAL total mas usd', #3
        'PRIVADOS total mas usd', #4
        'delete_2', #5
        'TOTAL dep usd', #6
        'PRIVADOS dep usd', #7
        'delete_3', #8
        'm2', #9
        'tipo_serie', #10 
    ],
    'PRESTAMOS': [
        'date',
        'ARS adelantos',
        'ARS documentos',
        'ARS hipotecarios',
        'ARS prendarios',
        'ARS personales',
        'ARS tarjetas',
        'ARS otros',
        'ARS total',
        'USD adelantos',
        'USD documentos',
        'USD hipotecarios',
        'USD prendarios',
        'USD personales',
        'USD tarjetas',
        'USD otros',
        'USD total',
        'delete_1',
        'USD sector privado',
        'delete_2',
        'total sector privado',
        'tipo_serie',
    ],
    'INSTRUMENTOS DEL BCRA': [
        'date',
        'pases pasivos total',
        'pases pasivos fci',
        'pases activos',
        'leliq y notaliq',
        'total lebac',
        'total lebac entidades',
        'lebac usd',
        'nocom',
        'tna pol mon',
        'tea pol mon',
        'pasivos 1d',
        'pasivos 7d',
        'activos 1d',
        'activos 7d',
        'TASA lebac 1m',
        'TASA lebac 2m',
        'TASA lebac 3m',
        'TASA lebac 4m',
        'TASA lebac 5m',
        'TASA lebac 6m',
        'TASA lebac 7m',
        'TASA lebac 8m',
        'TASA lebac 9m',
        'TASA lebac 10m',
        'TASA lebac 11m',
        'TASA lebac 12m',
        'TASA lebac 18m',
        'TASA lebac 24m',
        'TASA cer 6m',
        'TASA cer 12m',
        'TASA cer 18m',
        'TASA cer 24m',
        'TASA lebac usd ars 1m',
        'TASA lebac usd ars 6m',
        'TASA lebac usd ars 12m',
        'TASA lebac usd usd 1m',
        'TASA lebac usd usd 6m',
        'TASA lebac usd usd 12m'
    ]
}

list_aggregates = [
    'Base Monetaria',
    'Base Monetaria + Pasivos Remunerados',
    'M2',
    'M3',
    'Reservas',
    'Tipo de Cambio',
]

list_type_graph = [
    'Nominal',
    'Escala Logaritmica',
    'Variación Mensual',
    'Variación interanual',
]