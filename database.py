import random
class database:
    Names=["BBT SHELDON","BBT RAJ KOOTHRAPALLI,","BBT LEONARD,","BBT HOWARD WOLOWITZ,","BBT AMY FRRAH FAWLER,","VERONICA,","UNQ GAMER,","I M RUTHLESS,","SOUL MORTAL,","SPOUL REGALTOS,","8BIT_REBEL,"]
    Id=random.randrange(564748369,595874846)
    RATIO=random.uniform(1,5)
    Tier=["CONQUERER","ACE","CROWN","DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE"]
    Server=["ASIA","MIDDLE EAST","KRJP","NORTH AMERICA"]
    Win=random.randrange(10,30)
    Top_10=random.randrange(60,90)

 
    

class ans:
    def ans():
        return [random.choice(database.Names), 
        random.randrange(564748369,595874846),
        round(random.uniform(1,5), 2), 
        random.choice(database.Tier),
        random.choice(database.Server),
        random.randrange(10,30),
        random.randrange(60, 90),
        
         ]


