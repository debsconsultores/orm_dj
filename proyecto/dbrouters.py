class DBRouter:
    """
    Con este método db_for_read le decimos a Django que debe usar la base de datos de cada app
    """
    def db_for_read(self,model,**hints):
        if model._meta.app_label=='inv':
            return 'db_inv'
        return 'default'

    """
    Con el método db_for_write le decimos a Django qué base de datos debe usar para guardar los datos de nuestra aplicación
    """
    def db_for_write(self,model,**hints):
        print(model._meta.app_label,"<---Este es la app")
        if model._meta.app_label == 'inv':
            return 'db_inv'
        return 'default'

    """
    En esta sección Especificamos una relación entre dos elementos u objetos
    """
    def allow_realtion(self,elem1,elem2, **hints):
        # if elem1._meta.app_label == 'app1' and
        #    elem2._meta.app_label == 'inv':
        #    return True
        # return None
        return True

    """
    Indicamos si es que las migraciones se deben ejecutar en la base de datos 'inv'
    """
    def allow_migrate(self,db,app_label,model_name=None, **hints):
        # if app_label == 'inv':
        #     return db == 'inv'
        # return None
        return True