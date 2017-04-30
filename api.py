import shelve

def main():
    db = shelve.open("groot.db")
    try:
        db["columns"] = {1:"fname", 2:"lname",3:"weapon",4:"Lumberjack"}
        db["gamora"] = {"fname":"Gamora", "lname":"Unknown", "weapon":"Sword", "Lumberjack": "?"}
        db["quill"] = {"fname": "Star", "lname":"Lord", "weapon": "Guns", "Lumberjack": "?"}
        db["drax"] = {"fname": "Drax", "lname":"the Destroyer", "weapon": "Daggers", "Lumberjack": "?"}
    finally:
        db.close()
    db = shelve.open("groot.db")
    for x in db:
        if x != "columns":
            print("%s: %s" % (x, str(db[x])))
    for x in db["columns"]:
        print(x, db["columns"][x])

def delrow(db, rowkey):
    try:
        del db[rowkey]
    except:
        pass

if __name__ == "__main__":
    main()
