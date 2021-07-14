from flask import Flask,jsonify,request
app=Flask(__name__)
Task=[
    {
        "id":1,
        "title":"Buy Groceries",
        "description":"I want to buy some biscuits and some packets of rice",
        "done":False

    },
    {
        "id":2,
        "title":"Buy electronics",
        "description":"I want to buy some chargers and 1 smartphone",
        "done":False

    },
    {
        "id":3,
        "title":"Buy balls",
        "description":"I want to buy some cricket balls and 2 football",
        "done":False

    },
]

@app.route("/add_Data",methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "message":"Please provide the data"
        },404)
    task={
        "id":Task[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    Task.append(task)
    return jsonify({
        "Status":"Success",
        "message":"Task added successfully"
    },23)
@app.route("/get_Data")
def getData():
    return jsonify({
        "data":Task
    })

if(__name__=="__main__"):
    app.run()