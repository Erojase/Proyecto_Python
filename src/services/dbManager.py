import supabase as db
from src.components.colegio import *
import json

class DbManager:
    """
        Clase para controlar la base de datos
        
        Funciones:
        ---------
         - listAnime()
         - listUsers()
    """
    url = "https://vsfzxwsmptkuukibbjcq.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZzZnp4d3NtcHRrdXVraWJiamNxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjY4NzU4MTksImV4cCI6MTk4MjQ1MTgxOX0.KlPoTtVj4qbDIyFkXJE_00OmPN69fR2JTVsCMm_aBpg"

    supabase = db.create_client(url, key)
    
    
    def __init__(self) -> None:
        pass
    
    def listUsers(self) -> dict:
        """
            Lista Los usuarios de la base de datos
        """
        data = self.supabase.table('python_users').select('*').execute()
        return json.loads(json.dumps(data.data))
    
    def listAnimes(self) -> dict:
        data = self.supabase.table('animes').select('*').execute()
        return json.loads(json.dumps(data.data))
    
    def uploadAnimes(self, animes:list[dict]):
        pass
    
    def uploadHorario(self, listado:list[dict]):
        data = self.supabase.table('python_users')
        
        for hora in listado:
            data.insert({
                "nombre":hora._nombre,
                "tiempo":hora._tiempo,
                "grupo":hora._grupo,
                "profesor":hora._profesor
            }).execute()
    
    