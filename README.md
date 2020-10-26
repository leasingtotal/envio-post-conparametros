# envio-post-conparametros

# Instalacion

### Para esto, necesitamos ejecutar en el CMD:

pip install virtualenv

Una vez ya instalado el entorno virtual, debemos crear uno. Para crearlo, debemos utilizar el siguiente comando:

virtualenv -p python nombre_entorno

una vez lo hagamos, podemos activar el entorno en windows, accediendo a la ruta del entorno virtual, luego a la carpeta de script y luego activar sin cd. 
Por ejemplo, mi carpeta principal es esta:

Directory: C:\Users\soporte02\Desktop\ejemplo-pyt

dentro, esta mi entorno virtual llamado venv. Por lo cual, ejecuto:
.\venv\Scripts\activate

con ello, activamos el entorno. Para saber si realmente estamos en un entorno virtual, debemos tener el nombre del entorno 
entre parentesis antes de la ruta en la que nos encontramos:

(venv) PS C:\Users\soporte02\Desktop\ejemplo-pyt>

Una vez hagamos eso, ya podemos comenzar a instalar lo necesario para correr la aplicacion que es: 

pip install flask
pip install flask_cors
pip install jsonify
