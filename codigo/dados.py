colonia = {'energia':
               {'geracao':
                    {'solar': 40,
                     'eolica':25
                     },
                'baterias':{'capacidade_total':200,
                            'reserva_atual':120
                            }
                },
           'modulos': {'Habitacao':{'consumo':15,
                                    'essencial':True
                                    },
                       'Energia':{'consumo':8,
                                  'essencial':True
                                  },
                       'Suporte Medico':{'consumo':10,
                                         'essencial':True
                                         },
                       'Logistica':{'consumo':7,
                                    'essencial':False
                                    },
                       'Pesquisa Cientifica':{'consumo':5,
                                              'essencial':False
                                              }
                       }
           }

velocidades_vento=[6,8,10,12,14]
geracoes_eolicas=[15,19,24,28,34]
vento_previsto=11
