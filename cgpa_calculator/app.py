from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("app.html")


@app.route("/calculate", methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    num4 = request.form['num4']
 
   
    result = (float(num1) + float(num2) + float(num3) + float(num4))/4 
        
    x = "{:.2f}".format(result)
    y = str(x)
        
     
    return render_template('app.html', result= "You obtained " +y+ " out of 4")
    
    
        
if __name__ == '__main__':
	app.run(debug=True)
