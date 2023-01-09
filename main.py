from flask import Flask,render_template,request,redirect
import pymysql

app=Flask('__name__')  #creating an object of Flask class

@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost", user="root",password="Nitesh@123",database="todo_list")
        cu=db.cursor()
        q="select * from todo"
        cu.execute(q)
        data=cu.fetchall()
        return render_template('Dashboard.html',d=data) 
    except Exception as e:
        return "Error"
    

@app.route('/create' )
def create():
    return render_template('form.html')

@app.route('/store', methods=['POST'] )
def store():
    n=request.form['n']
    a=request.form['a']
    s=request.form['s']
    dst=request.form['dst']
    
    try:
        db=pymysql.connect(host="localhost", user="root",password="Nitesh@123",database="todo_list")
        cu=db.cursor()
        q="insert into todo (task_name,task_description,task_time,task_priority) values('{}','{}','{}','{}')".format(n,a,s,dst)
        cu.execute(q)
        db.commit()
        return redirect('/')  
    except Exception as e:
               return "Error"
        
        
@app.route('/delete/<rid>')
def delete(rid):
        try:
            db=pymysql.connect(host="localhost", user="root",password="Nitesh@123",database="todo_list")
            cu=db.cursor()
            q="delete from todo where sr='{}'".format(rid)
            cu.execute(q)
            db.commit()
            return redirect('/')
        except Exception as e:
            return ("error",+e)
                
@app.route('/edit/<rid>')
def edit(rid):
        try:
            db=pymysql.connect(host="localhost", user="root",password="Nitesh@123",database="todo_list")
            cu=db.cursor()
            q="select * from todo where sr='{}'".format(rid)
            cu.execute(q)
            data=cu.fetchone()
            return render_template('editform.html',d=data) 
        except Exception as e:
            return "Error"
    
@app.route('/update/<rid>', methods=['POST'])
def update(rid):
                un=request.form['n']
                ua=request.form['a']
                us=request.form['s']
                udst=request.form['dst']
                try:
                    db=pymysql.connect(host="localhost",user="root",password="Nitesh@123",database="todo_list")
                    cu=db.cursor()#cu is the variable to hold the cursor
                    q="update todo set task_name='{}',task_description='{}',task_time='{}',task_priority='{}' where sr='{}'".format(un,ua,us,udst,rid)
                    cu.execute(q)
                    db.commit()
                    return redirect('/')
                except Exception as e:
                    return("Error",e)
        
app.run(debug=True)

