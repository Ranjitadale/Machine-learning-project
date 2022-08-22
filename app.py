from flask import Flask
app=Flask(__name__)

@app.route("/",method=['GET','POST'])
def idex():
    return "Starting Machine Learning Projecr"


if __name__=="__main__":
    app.run(debug=True)