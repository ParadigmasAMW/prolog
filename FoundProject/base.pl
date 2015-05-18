:- dynamic software/9.
:- dynamic linguagem/2.
:- dynamic categoria/2.
:- dynamic licenca/2.
:- dynamic plataforma/2.
:- dynamic tamanho/2.
:- dynamic tempo_final/2.
:- dynamic tempo_incial/2.
:- dynamic valor/2.

%Software(Nome, categoria, linguagem, licença, plataforma,tamanho, tempo inicial, tempo final, valor).

software(atom,ide,coffescript,mit,desktop,_,_,_,0).
software(savant,educacional,php,'',web,_,'2013-4-17','2013-7-23',5000).
software('Nazario Contruções',fincanceiro,python,'',web,_,'2014-5-1','2014-7-7',2500).
software(notepad,ide,'c++',gpl,desktop,_,_,_,0).
software('devc++',ide,delphi,gpl,desktop,_,_,_,0).
software(codeBlocks,ide,cplusplus,gpl,desktop,_,_,_,0).
software(eclipse,ide,java,epl,desktop,_,_,_,0).
software(netbeans,ide,java,freeware,desktop,_,_,_,0).
software(gimp,'editor de imagem',c,gplv3,desktop,_,_,_,0).
software(dauphine,game,javascript,'',web,_,_,_,10000).

%Especializações

categoria(Nome, Categoria):- software(Nome,Categoria,_,_,_,_,_,_).
linguagem(Nome, Linguagem):- software(Nome,_,Linguagem,_,_,_,_,_,_).
licenca(Nome, Licenca):- software(Nome,_,_,Licenca,_,_,_,_,_).
plataforma(Nome, Plataforma):- software(Nome,_,_,_,Plataforma,_,_,_,_).
tamanho(Nome, Tamanho):- software(Nome,_,_,_,_,Tamanho,_,_,_).
tempo_final(Nome, TempoIncial):- software(Nome,_,_,_,_,_,TempoIncial,_,_).
tempo_inical(Nome,TempoFinal):- software(Nome,_,_,_,_,_,_,TempoFinal,_).
valor(Nome,Valor):- software(Nome,_,_,_,_,_,_,_,Valor).