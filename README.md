# Api_Django_Ecommerce



<div style="display: inline_block"><br>
<h1 align="center">
  <img alt="KenzieKommerce" title="KenzieKommerce" src="https://kenzie.com.br/_next/image?url=%2Fimages%2Flogo.png&w=640&q=75" width="100px" />
</h1>
  <p align="center">Este é o backend da aplicação de e-commerce do quinto módulo da Kenzie-Academy-Brasil, desenvolvida em python e django, esta aplicação
  foi feita no intuito de demonstrar os conhecimentos que os desenvolvedores adquiriram sobre python nos últimos 2 meses de aprendizado de python. <p/>
  
  <h5 align="center">Feito por: Victor Guterres, Gabriel Machado, Gabriela Fontoura, Guileano Gadea </h5>  
</div>

## **Endpoints**

A API tem um total de 19 endpoints, sendo em volta principalmente do usuário onde ele pode ser: Cliente, Vendedor, Administrador - podendo cadastrar seu perfil, selecionar e comprar produtos se o usuário for cliente ou criar e editar caso o usuário for vendedor/administrador(na regra de negócios de nossa aplicação o vendedor também deve ser um cliente) ele será capaz de editar e excluir produtos . <br/>

A url base da API é https://ecommerce-g42.onrender.com/

Diagrama do Der https://drive.google.com/file/d/1dWz9-AqqLakLX_afLU5QKIvF-YEVYW0V/view" 


## Rotas que não precisam de autenticação

<h2 align ='center'> Criando usuário </h2>
 
 Nessa aplicação o usuário pode se cadastrar utilizando seu primeiro e último nome, seu nome de usuário e como padrão a role(função) dele
 vem como cliente(apenas administradores podem criar outros administradores e vendedores) .

```json
{
		"first_name": "Pedro",
		"last_name": "Castro",
		"email": "Pc@mail.com",
		"username": "PcGamerSP",
		"password": "1234"
}

```

`POST /users - FORMATO DA RESPOSTA - STATUS 201`

```json
{
		"first_name": "Pedro",
		"last_name": "Castro",
		"role": "Client",
		"email": "Pc@mail.com",
		"username": "PcGamerSP"
}

```
em caso de erro:

```json
{
	"first_name": [
		"This field is required."
	],
	"last_name": [
		"This field is required."
	],
	"username": [
		"This field is required."
	],
	"email": [
		"This field is required."
	],
	"password": [
		"This field is required."
	]
}
```

<h2 align ='center'> Login de usuário </h2>


body:

```json
       {
	"username": "John Doe",	
	"password":1234
	}
```


`POST /users/login - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NDI0NzU4MiwiaWF0IjoxNjgzNjQyNzgyLCJqdGkiOiJhNGM0YzdhN2YxNjg0NmU4ODczNTFmYTJkOWY1NDkxMyIsInVzZXJfaWQiOjJ9.17ZJeaNgKZH5A4OclYufT_ErMIKcr_g8zjLm6Th36Jo",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNjk2NzgyLCJpYXQiOjE2ODM2NDI3ODIsImp0aSI6ImFmYzkzYWVkOGEzOTQwMDVhODM3Yzk5ZGVlOTlkMjk3IiwidXNlcl9pZCI6Mn0.xqTLZBTDdIuBcLGSBxpj4BCVFKgu-UbOxw1Nu-s24Aw"
}
```




## Rotas que precisam de autenticação

<h2 align ='center'> Listando usuário </h2>
 
 Nessa aplicação o usuário deve ser administrador para poder listar os usuários .
 
 ` GET /users/all - FORMATO DA RESPOSTA - STATUS 200`

```json
	"count": 2,
	"next": null,
	"previous": null,
	"results"[
{
		"first_name": "Pedro",
		"last_name": "Castro",
		"role": "Client",
		"email": "Pc@mail.com",
		"username": "PcGamerSP"
},
{
		"first_name": "Larissa",
		"last_name": "Torres",
		"role": "Client",
		"email": "Kenzie@mail.com",
		"username": "Random"
},
{
		"first_name": "John",
		"last_name": "Doe",
		"role": "Client",
		"email": "Kenzie@mail.com",
		"username": "Random"
}
,
{
		"first_name": "Roberto",
		"last_name": "Schrödinger",
		"role": "Client",
		"email": "Kenzie@mail.com",
		"username": "Random"
}
,
{
		"first_name": "Alberto",
		"last_name": "Leone",
		"role": "Client",
		"email": "Kenzie@mail.com",
		"username": "Random"
}
]
```
Lembrando que no cabeçalho da resposta, temos as informações sobre a paginação, e o nextUrl para acessar a próxima página.

Cabeçalho da resposta:

> count: <br/>
> page:  <br/>
> perPage: 

Em caso de erro na autorização ou caso o usuário não passe o token de autorização na requisição:

` GET /users/all - FORMATO DA RESPOSTA - STATUS 401 unauthorized`


```json

{
	"detail": "You do not have the authorization to perform this action."
}


```
<h2 align ='center'> Dando update e deletando usuários </h2>

Utilizandoa a rota /users/:id é possível fazer a pesquisa do usuário, update e o delete pegando o id do usuário, somente o usuário
, com exceção do admin pode editar e deletar o próprio delete, caso o usuário tente atualizar o perfil de outro usuário .

essa requisição não precisa de um corpo

` GET /users/:id - FORMATO DA RESPOSTA - STATUS 200 unauthorized`


```json

{
		
	"email": "Pc@Gmail.com"
}


```

```json
{
		"first_name": "Pedro",
		"last_name": "Castro",
		"role": "Client",
		"email": "Pc@Gmail.com",
		"username": "PcGamerSP"
}

```
em caso de erro na autorização:



```json
{
	"detail": "You do not have the authorization to perform this action."
}
```

















