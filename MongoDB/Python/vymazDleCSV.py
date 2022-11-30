# nacte csv a vymaze z databaze
from pymongo import MongoClient
from bson.objectid import ObjectId


class nactiCsvData:

    def __init__(self):

        self.uplnaCesta = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVASCRIPT\\NODEJS\\YOUTUBE - SOCKETS\\tools\\MongoDB\\dataMongo\\deleteFiles.csv"
        self.nazvyIdProVymazani = self.nactiIdProVymazani()


        try:
            conn = MongoClient(port=27017)
            print("Connected successfully!!!")

            # database
            db = conn.database
            self.collection = db.OOFEM

            # vymaze data z databaze
            self.vymazDataZDatabaze()

        except:
            print("Could not connect to MongoDB")



    def nactiIdProVymazani(self):

        with open(self.uplnaCesta ) as f:
            lines = f.readlines()

        return(lines)


    def vymazDataZDatabaze(self):

        for i in range(0, len(self.nazvyIdProVymazani)):
            idProVymazani = self.nazvyIdProVymazani[i]
            myquery = self.sestavMyQuery(idProVymazani)

            # vymaze soubor
            self.collection.delete_many(myquery)


    def sestavMyQuery(self, idProVymazani):

        idProVymazani = idProVymazani.replace("\n", "")
        idProVymazani = idProVymazani.replace(" ", "")
        myquery = {"_id": ObjectId(idProVymazani)}

        return(myquery)