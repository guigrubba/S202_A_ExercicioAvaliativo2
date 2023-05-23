from family_database import FamilyDataBase

db = FamilyDataBase("bolt://54.89.205.193:7687", "neo4j", "depths-hyphens-sword")

print(db.get_animals())
print(db.get_teachers())
print(db.get_mothers())