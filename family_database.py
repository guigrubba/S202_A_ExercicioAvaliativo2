from neo4j import GraphDatabase

class FamilyDataBase:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def _execute_query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters or {})
            return [record for record in result]

    def get_animals(self):
        query = "MATCH (a:Animal) RETURN a.nome as nome"
        return [record['nome'] for record in self._execute_query(query)]
    
    def get_teachers(self):
        query = "MATCH (p:Professora) RETURN p.nome as nome"
        return [record['nome'] for record in self._execute_query(query)]
    
    def get_mothers(self):
        query = "MATCH (m)-[:MAE_DE]->() RETURN DISTINCT m.nome as nome"
        return [record['nome'] for record in self._execute_query(query)]
