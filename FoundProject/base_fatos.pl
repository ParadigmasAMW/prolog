:- dynamic software/4
:- dynamic pessoa/3

#software(nome, categorias, linguagem, lincença)
#pessoa(nome, linguagem preferida, @dicas)

software(atom,ide,coffescript,copyright).
software(notepad,ide,c++,gpl).
software(devc++,ide,delphi,gpl).
software(code::blocks,ide,c++,gpl).
software(eclipse,ide,java,epl).
software(netbeans,ide,java,freeware).

pessoa(wilker,c++).
pessoa(alvaro,ruby).
pessoa(matheus,python).

#licenças Livres

livre(gpl).
livre(agpl). 