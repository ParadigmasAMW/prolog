:- dynamic software/10.
:- dynamic linguagem/2.
:- dynamic categoria/2.
:- dynamic licenca/2.
:- dynamic plataforma/2.
:- dynamic tamanho/2.
:- dynamic tempo_final/2.
:- dynamic tempo_incial/2.
:- dynamic valor/2.

%Software(Nome, categoria, linguagem, licença, plataforma,tamanho, tempo inicial, tempo final, valor).

software('1','atom','ide','coffescript','mit','desktop','','','','0').
software('2','savant','educacional','php','','web','','17/04/2013','23/07/2013','5000').
software('3','Nazario Contrucoes','fincanceiro','python','','web','','01/05/2014','07/07/2014','2500').
software('4','notepad','ide','c++','gpl','desktop','','','','0').
software('5','devc++','ide','delphi','gpl','desktop','','','','0').
software('6','codeBlocks','ide','cplusplus','gpl','desktop','','','','0').
software('7','eclipse','ide','java','epl','desktop','','','','0').
software('8','netbeans','ide','java','freeware','desktop','','','','0').
software('9','gimp','editor de imagem','c','gplv3','desktop','','','','0').
software('10','dauphine','game','javascript','','web','','','','10000').

%Especializações

categoria(Nome, Categoria):- software(Nome,Categoria,_,_,_,_,_,_).
linguagem(Nome, Linguagem):- software(Nome,_,Linguagem,_,_,_,_,_,_).
licenca(Nome, Licenca):- software(Nome,_,_,Licenca,_,_,_,_,_).
plataforma(Nome, Plataforma):- software(Nome,_,_,_,Plataforma,_,_,_,_).
tamanho(Nome, Tamanho):- software(Nome,_,_,_,_,Tamanho,_,_,_).
tempo_final(Nome, TempoIncial):- software(Nome,_,_,_,_,_,TempoIncial,_,_).
tempo_inical(Nome,TempoFinal):- software(Nome,_,_,_,_,_,_,TempoFinal,_).
valor(Nome,Valor):- software(Nome,_,_,_,_,_,_,_,Valor).