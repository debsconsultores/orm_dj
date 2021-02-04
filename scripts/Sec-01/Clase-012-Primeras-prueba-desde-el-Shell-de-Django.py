# Importar Modelo Categoria
from app1.models import Categoria

# Devolver todos los objetos
Categoria.objects.all()
# <QuerySet [<Categoria: Programación>, <Categoria: Base de Datos>, <Categoria: Servidores>, <Categoria: Redes>, <Categoria: Soporte>, <Categoria: Administración>]>