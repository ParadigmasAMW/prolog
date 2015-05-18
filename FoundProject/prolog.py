# -*- coding: utf8 -*-
from pyswip import Prolog

prolog = Prolog()

prolog.consult('base.pro')
# prolog.retract("software('Nazario Contruções',fincanceiro,python,'',web,_,'2014-5-1','2014-7-7',2500)")
results = prolog.query("software(Nome,Categoria,Linguagem,Licensa,Plataforma,Tamanho,DataI,DataF,Valor )")
for result in results:
    print result
