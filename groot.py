import shelve, globe, gspread, csv
from inspect import signature, _empty
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/user256/PycharmProjects/passwords/sheets_client_secrets.json', scope)
client = gspread.authorize(creds)

def main():
    for dbsource in ["gdocs","local"]:
        dosheet(dbsource)
        print(globe.fargs)

def dosheet(dbsource):
    db = ""
    if dbsource =="local":
        db = shelve.open("groot.db")
        with open("database.csv") as file:
            reader = csv.reader(file)
            for rowdex, arow in enumerate(reader):
                db[str(rowdex + 1)] = arow
        db.close()
        db = shelve.open("groot.db")
        #globe.lrow = len(db)
        for rowkey in sorted(db):
            dorow(rowkey, db[rowkey])
    elif dbsource =="gdocs":
        gwks = client.open("Use This").sheet1
        for rowdex in range(1, gwks.row_count):
            arow = gwks.row_values(rowdex)
            if arow:
                dorow(str(rowdex), arow)
            else:
                break
            pass #print(rowdex)
    else:
        pass

def dorow(rownum, arow):
    if rownum == "1":
        dofuncs(arow)
    else:
        print(arow)

def Func1():
    return "Ni!"

def Func2(param1, param2, status="Okay"):
    return "I'm ok!"

def dofuncs(arow):
    fargs = {}
    for rowdex, fname in enumerate(arow):
        rowdex += 1
        if fname in globals():
            fargs[rowdex] = {}
            sig = signature(eval(fname))
            for param in sig.parameters.values():
                pname = param.name
                pdefault = param.default
                if pdefault is _empty:
                    fargs[rowdex][pname] = None
                else:
                    fargs[rowdex][pname] = pdefault
    globe.fargs = fargs

def delrow(db, rowkey):
        try:
            del db[rowkey]
        except:
            pass

if __name__ == "__main__":
    main()

