# hello-flask
Comenzamos el desarrollo web en el bootcamp 

# A tener en cuenta
Flask necesita un servidor web para que la app funcione. El servidor web es el que se encarga de recibir las peticiones y enviarlas a nuestro programa en Flask. Flask le da el resultado al servidor web y el servidor web se lo envía al navegador.

Para no complicar el escenario en el momento de comenzar a desarrollar nuestra aplicación, Flask nos proporciona un servidor SOLAMENTE PARA DESASARROLLO. Es decir, solo está peparado para facilitarnos las pruebas en nuestra máquina local.

# Variables de entorno
Linux / Mac export FLASK_APP=hello export FLASK_DEBUG=True

Windows set FLASK_APP=hello set FLASK_DEBUG=True