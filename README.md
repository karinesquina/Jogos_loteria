O script tem como objetivo:

1. Conectar-se com a basde de dados de resultados dos jogos de "Mega Sena", "Quina" e "Loto Fácil";
2. Fazer o download do arquivo zip disponível no site oficial da Caixa Econômica Federal;
3. Descompactar os arquivos para dentro de uma pasta com a data do dia da extração;
4. Tranformar o arquivo HTML para CSV, separado por ";";
5. Tratar os campos "&nbsp" da base de dados;
6. Salvar o arquivo tratado para futura análise dos especialistas.

#Passo a passo para rodar o script

1. Faça o download do arquivo 'main.py';
2. Abra o cmd (em caso de windows) ou o prompt de comando do seu O.S.;
3. Acesse a pasta onde está salvo o arquivo 'main.py', utilizando os comandos pertinentes de seu O.S.;
3. Digite: python main.py parametro que deseja (megasena, quina, lotofacil). Ex.: python main.py megasena.

#Requisito para rodar o script

Python 3.9.0

#Função do script

O Script irá criar 3 pastas conforme abaixo:

1. Pasta Raw - recebe os arquivos extraidos da plataforma no formato 'html', dentro de uma pasta com a data do dia da extração;
2. Pasta Swamp - recebe o arquivo convertido de html para csv;
3. Pasta Lake - recebe o arquivo final tratado.

Você pode rodar os 3 jogos (separadamente) sem precisar deletar as pastas, pois os mesmos criam subpastas dentro das matrizes raw, swamp e lake.

