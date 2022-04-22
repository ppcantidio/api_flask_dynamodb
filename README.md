### Introdução
Essa API utiliza a API Genius para trazer as 10 músicas mais famosas de um artista.

### Fluxo da aplicação
![](https://i.ibb.co/Dfkj8HM/Diagrama-em-branco-1.png)

### Tecnologias
- Python 3
- Flask
- Redis
- DynamoDB

### Como rodar
Para rodar a API você irá precisara:
- Ter o redis instalado e executando na sua maquina.
- Conta AWS.

A API utiliza a versão web do DynamoDB porém para utilizar a versão local basta alterar no arquivo .env:
``` sh
PRODUCTION==0
```

Já para utilizar sua conta AWS, deve preencher os campos AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY no arquivo .env e alterar:
``` sh
PRODUCTION==1
```

Para instalar as bibliotecas utilize:
``` sh
pip install -r requirements.txt
```

Após isso só executar o arquivo run.py

### Como consumir
- Utilize o método POST para rota:
``` sh
http://127.0.0.1:5000/api/v1/artists
```

- No body envie os seguinte parâmetros: 
```sh
{
	"artist": "Pedro Sampaio"
}
```

- Caso você não queira utilizar o cache, na url passe o seguinte parâmetro:
``` sh
http://127.0.0.1:5000/api/v1/artistas/?cache=False
```
