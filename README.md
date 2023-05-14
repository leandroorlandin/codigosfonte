Neste exemplo, criamos uma classe chamada DeployJsonUpdater que executa as quatro etapas:
  1 - recebe um "deploy.json" em formato JSON com apenas um campo chamado "host" e carrega o mesmo em memória
  2 - altera o conteúdo do campo "host" na variável que está em memória para um conteúdo fixo "XPTO", de uma variável interna
  3 - cria novo campo chamado no json chamado "timestamp_alteracao", o qual conterá o timestamp do horário de execução do programa
  4 - atualiza o arquivo "deploy.json" com os 2 campos ("host" e "timestamp_alteracao") atualizados.

Na primeira etapa, usamos o método loadJsonFromFile para carregar o arquivo JSON em memória em um objeto JSONObject. O caminho do arquivo é definido na constante JSON_FILE_PATH.

Na segunda etapa, atualizamos o valor do campo "host" para o valor fixo "XPTO".

Na terceira etapa, adicionamos um novo campo chamado "timestamp_alteracao" com o valor atual do timestamp formatado como uma string.

Por fim, na quarta etapa, usamos o método updateJsonFile para atualizar o arquivo JSON com as alterações feitas na etapa anterior.

Este é apenas um exemplo simples de como executar essas etapas em Java. É importante lembrar que este código pode ser mais apropriado para casos simples e pequenos arquivos JSON. Para arquivos JSON mais complexos e grandes, pode ser mais adequado usar uma biblioteca ou framework especializado em JSON.
