from fastapi import FastAPI,requests
from pydantic import BaseModel
import uvicorn
import mysql.connector

app = FastAPI()

class model(BaseModel):
    Deal_date =str
    security_code =str
    Securite_name =str
    Client_Name	 =str
    Deal_Type =str
    Quantity	=str
    Price =str

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="Bseindia")
cur=mydb.cursor()
@app.get("/alldetails")
def alldetails():
    cur.execute("select * from Bseindia")
    data=cur.fetchall()
    df=[]
    for i in data:
       dd={"Deal_date":i[0],
        "security_code":i[1],
        "Securite_name":i[2],
        "Client_Name":i[3],
        "Deal_Type":i[4],
        "Quantity":i[5],
        "Price":i[6]}
       df.append(dd)
    return df

@app.get("/data/{id}")
def selected_data(id):
    try:
        cur.execute(f"select * from Bseindia where security_code={id}")
        ik=cur.fetchall()
        print(f"{len(i)} data")
        df=[]
        for i in ik:
            dd={"Deal_date":i[0],
                "security_code":i[1],
                "Securite_name":i[2],
                "Client_Name":i[3],
                "Deal_Type":i[4],
                "Quantity":i[5],
                "Price":i[6]}
            df.append(dd)
        return df
    except:
       return f"security code {id} not in db"

@app.get("/delete/{id}")
def delete_data(id):
   try:
    cur.execute(f"Delete from Bseindia where security_code={id}")
    mydb.commit()
    return f"security code {id} removed databases successfuly"
   except:
      return f"security code {id} not available in db"


@app.get("/data/update/{id}")
def selected_data(id:int,item:model):
    try:
        query=f'''UPDATE table_name
        SET  "Deal_date"={item.Deal_date},
                "security_code"={item.security_code},
                "Securite_name"={item.Securite_name},
                "Client_Name"={item.Client_Name},
                "Deal_Type"={item.Deal_Type},
                "Quantity"={item.Quantity},
                "Price"={item.Price}
        WHERE condition'''
        cur.execute(query)
        mydb.commit()

    except:
      return "Security code not available "
    
if __name__ == "__main__":
   uvicorn.run("Api:app", host="127.0.0.1", port=8000, reload=True)