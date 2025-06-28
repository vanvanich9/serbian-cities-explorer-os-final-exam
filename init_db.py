from database import Base, engine, City, SessionLocal


def create_tables():
    Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    if db.query(City).first():
        return

    cities_data = [
        {
            "name": "Belgrade",
            "description": "Belgrade is the capital and largest city of Serbia. It is located at the confluence of the Sava and Danube rivers and the crossroads of the Pannonian Plain and the Balkan Peninsula. Belgrade has a rich history dating back to ancient times and is known for its vibrant nightlife, cultural institutions, and historical landmarks.",
            "population": 1688667,
            "area": 3235.0,
            "region": "Central Serbia",
            "founded_year": 279,
            "image": "belgrade.jpg"
        },
        {
            "name": "Novi Sad",
            "description": "Novi Sad is the second largest city in Serbia and the capital of the autonomous province of Vojvodina. It is known for its Petrovaradin Fortress, the EXIT music festival, and its rich cultural heritage. The city is often called the 'Serbian Athens' due to its cultural significance.",
            "population": 307760,
            "area": 699.0,
            "region": "Vojvodina",
            "founded_year": 1694,
            "image": "novi-sad.jpg"
        },
        {
            "name": "Niš",
            "description": "Niš is the third largest city in Serbia and the administrative center of the Nišava District. It is one of the oldest cities in the Balkans and Europe, with a history spanning over 2,000 years. The city is known for its historical sites, including the Skull Tower and Niš Fortress.",
            "population": 183164,
            "area": 596.7,
            "region": "Southern Serbia",
            "founded_year": -279,
            "image": "nis.jpg"
        },
        {
            "name": "Kragujevac",
            "description": "Kragujevac is the fourth largest city in Serbia and the administrative center of the Šumadija District. It was the first capital of modern Serbia and is known for its automotive industry, particularly the Zastava automobile factory. The city has a rich cultural and educational heritage.",
            "population": 150835,
            "area": 835,
            "region": "Šumadija",
            "founded_year": 1476,
            "image": "kragujevac.jpg"
        },
        {
            "name": "Subotica",
            "description": "Subotica is the fifth largest city in Serbia and the second largest city in Vojvodina. It is known for its beautiful Art Nouveau architecture, particularly the City Hall and Synagogue. The city has a diverse ethnic population and is located near the border with Hungary.",
            "population": 105681,
            "area": 1007.5,
            "region": "Vojvodina",
            "founded_year": 1391,
            "image": "subotica.jpg"
        },
        {
            "name": "Zrenjanin",
            "description": "Zrenjanin is a city in the autonomous province of Vojvodina, Serbia. It is the administrative center of the Central Banat District. The city is known for its industrial heritage, particularly in the food processing and chemical industries. It has a rich cultural life and historical architecture.",
            "population": 123362,
            "area": 1325.9,
            "region": "Vojvodina",
            "founded_year": 1326,
            "image": "zrenjanin.jpg"
        },
        {
            "name": "Pančevo",
            "description": "Pančevo is a city in the autonomous province of Vojvodina, Serbia. It is the administrative center of the South Banat District. The city is known for its industrial heritage, particularly in oil refining and chemical production. It has a rich cultural scene and historical landmarks.",
            "population": 123414,
            "area": 756.0,
            "region": "Vojvodina",
            "founded_year": 1153,
            "image": "pancevo.jpg"
        },
        {
            "name": "Čačak",
            "description": "Čačak is a city in central Serbia and the administrative center of the Moravica District. It is known for its natural beauty, particularly the Ovčar-Kablar Gorge and the West Morava River. The city has a rich cultural heritage and is a popular tourist destination.",
            "population": 115337,
            "area": 636.0,
            "region": "Central Serbia",
            "founded_year": 1408,
            "image": "cacak.jpg"
        },
        {
            "name": "Kraljevo",
            "description": "Kraljevo is a city in central Serbia and the administrative center of the Raška District. It is known for the Žiča Monastery, one of the most important Serbian Orthodox monasteries. The city has a rich historical heritage and is located in a beautiful natural setting.",
            "population": 125488,
            "area": 1530,
            "region": "Central Serbia",
            "founded_year": 1476,
            "image": "kraljevo.jpg"
        }
    ]

    for city_data in cities_data:
        city = City(**city_data)
        db.add(city)
    
    db.commit()
    db.close()


if __name__ == "__main__":
    create_tables()
    init_db()
    print("Database initialized with Serbian cities data!")
