from flask import Flask, render_template,request,url_for,redirect
import pypyodbc
Connection=pypyodbc.connect('Driver={sql server};'
                          'server=NIKESH;'
                          'Database=restaurent;'
                          'Trusted_Connection=yes;')
cursor=Connection.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    cursor.execute('select * from Items')
    data=cursor.fetchall()
    return render_template("index.html",items=data)


@app.route('/add' , methods=['GET'])
def additem():
   name=request.args.get('itemname')
   cat=request.args.get('category')
   price=request.args.get('price')
   dis=request.args.get('dis')
   pic=request.args.get('pic')
   cursor.execute('insert into Items (name,category,price,discription,pic) values (?,?,?,?,?)',[name,cat,price,dis,pic])
   cursor.commit()
   return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute('delete from Items where id=?',[id])
    cursor.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
