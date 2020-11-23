O script tem como objetivo fazer o download dos resultados de 3 tipos de jogos da loteria disponíveis no site da caixa, sendo eles: Mega Sena, Loto Fácil e Quina.

#Passo a passo para rodar o script

1. Faça o download do arquivo 'main.py';
2. Abra o cmd (em caso de windows) ou o prompt de comando do seu O.S.;
3. Acesse a pasta onde está salvo o arquivo 'main.py', utilizando os comandos pertinentes de seu O.S.;
3. Digite: python main.py parametro que deseja (megasena, quina, lotofacil). Ex.: python main.py megasena.

#Requisito para rodar o script

Python 3.9.0

#Função do script

O Script irá criar 3 pastas conforme abaixo:

1. Pasta Raw - recebe os arquivos extraidos da plataforma no formato 'html';
2. Pasta Swamp - recebe o arquivo convertido de html para csv;
3. Pasta Lake - recebe o arquivo final tratado.


