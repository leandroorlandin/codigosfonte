Segue um exemplo de programa em Java que lê um arquivo YAML com o campo "host", altera o conteúdo do campo "host" para "XPTO", adiciona um novo campo "timestamp_alteracao" com o horário atual e salva o arquivo YAML atualizado:

Para usar esse código, é necessário adicionar a biblioteca SnakeYAML ao projeto. Se estiver usando o Maven, basta adicionar a seguinte dependência ao arquivo pom.xml:
<dependency>
    <groupId>org.yaml</groupId>
    <artifactId>snakeyaml</artifactId>
    <version>1.29</version>
</dependency>

Assumindo que o arquivo YAML de entrada está na mesma pasta que o arquivo DeployUpdater.java e se chama deploy.yaml, a execução do programa irá atualizar o arquivo deploy.yaml com os campos "host" e "timestamp_alteracao" atualizados.
