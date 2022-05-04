### url base: https://vacinacaowilliangeno.herokuapp.com

## POST => /api/vacinas
### Corpo da requisição:

```json
        {
            "cpf": "string (12345678910)",
		    "health_unit_name": "string",
		    "name": "string",
		    "vaccine_name": "string"
        }
```	
### Resposta:

       retorna o item creato e status code 200.
    
## GET => /api/vacinas
### Resposta: 
        retorna  o item cadastrado em formato de objeto, caso haja mais que um retorna uma lista de objetos 



