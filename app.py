from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
import matplotlib.pyplot as pl

app = Flask(__name__)

connection = mysql.connector.connect(host="localhost",user='root',password='',database='proprty_mgr')
mycursor = connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fgtpswd')
def fgtpswd():
    return render_template('/forgotpswd.html')


@app.route('/fgtpsw',methods=['GET','POST'])
def fgtpsw():
    if request.method=='post':
        username=request.form.get('username')
        password=request.form.get('password')
        rptpassword=request.form.get('rptpassword')
        
        query='UPDATE `accounts` SET `pswd`=%s WHERE `email`=%s'
        data=(password,username)
        mycursor.execute(query,data)
        connection.commit()
    return render_template('/forgotpswd.html',msg='Password changed successfully!')

            
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/home')
def hom():
    return render_template('home.html')

@app.route('/',methods=['GET','POST'])
def login():
    uname = request.form['username']
    pwd = request.form['password']
    data=(uname, pwd)
    query='SELECT * FROM accounts WHERE  email = %s AND pswd = %s'
    mycursor.execute(query,data)
    account = mycursor.fetchone()
    if account:
        if uname=='admin@gmail.com' and pwd=='admin':
            return render_template('admin_home.html',msg='welcome')
            
        else:
            msg='Welcome User'
            return render_template('home.html',msg=msg)
    
    else:
        msg='Incorrect username/password!'
        render_template('index.html',msg=msg)
   

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        pswd=request.form.get('psw')
        rpsw=request.form.get('psw-repeat')
        ph=request.form.get('phno')

        query='INSERT INTO `accounts`(`name`, `email`, `phno`, `pswd`, `rptpswd`) VALUES(%s,%s,%s,%s,%s)'
        data=(name,email,ph,pswd,rpsw)

        mycursor.execute(query,data)
        connection.commit()
        return render_template('/home.html',msg='Welcome User!')
    return render_template('register.html')


@app.route('/addpr')
def addpr():
    return render_template('addp.html',)


@app.route('/add')
def add():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        pswd=request.form.get('psw')
        rpsw=request.form.get('psw-repeat')
        ph=request.form.get('phno')

        query='INSERT INTO `accounts`(`name`, `email`, `phno`, `pswd`, `rptpswd`) VALUES(%s,%s,%s,%s,%s)'
        data=(name,email,ph,pswd,rpsw)

        mycursor.execute(query,data)
        connection.commit()
        return render_template('/register.html',msg='Added Successfully!')
    return render_template('register.html')
   
@app.route('/addp', methods=['GET','POST'])
def addp():
    if request.method=='POST':
       
        MSSubClas=request.form['MSSubClass']
        MSZoning=request.form['MSZoning']
        Street=request.form['Street']
        LotArea=request.form.get('LotArea')
        LotShape=request.form['LotShape']
        LandContour=request.form['LandContour']
        Utilities=request.form['Utilities']
        LotConfig=request.form['LotConfig']
        LandSlope=request.form['LandSlope']
        Neighborhood=request.form['Neighborhood']
        Condition1=request.form['Condition1']
        Condition2=request.form['Condition2']
        BldgType=request.form['BldgType']
        HouseStyle=request.form['HouseStyle']
        OverallQual=request.form['OverallQual']
        OverallCond=request.form['OverallCond']
        YearBuilt=request.form.get('YearBuilt')
        RoofStyle=request.form['RoofStyle']
        RoofMatl=request.form['RoofMatl']
        Exterior1st=request.form['Exterior1st']
        Exterior2nd=request.form['Exterior2nd']
        MasVnrType=request.form['MasVnrType']
        MasVnrArea=request.form.get('MasVnrArea')
        ExterQual=request.form['ExterQual']
        ExterCond=request.form['ExterCond']
        
        Foundation=request.form['Foundation']
        BsmtCond=request.form['BsmtCond']
        Electrical=request.form['Electrical']
        FstFlrSF=request.form.get('1stFlrSF')
        SndFlrSF=request.form.get('2ndFlrSF')
        SalePrice=request.form.get('SalePrice')

        query = 'INSERT INTO `propertydata`(`MSSubClass`, `MSZoning`, `LotArea`, `Street`, `LotShape`, `LandContour`, `Utilities`, `LotConfig`, `LandSlope`, `Neighborhood`, `Condition1`, `Condition2`, `BldgType`, `HouseStyle`, `OverallQual`, `OverallCond`, `YearBuilt`, `RoofStyle`, `RoofMatl`, `Exterior1st`, `Exterior2nd`, `MasVnrType`, `MasVnrArea`, `ExterQual`, `ExterCond`, `Foundation`,`BsmtCond`, `Electrical`, `1stFlrSF`, `2ndFlrSF`, `SalePrice`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data=(MSSubClas,MSZoning, LotArea, Street, LotShape, LandContour, Utilities, LotConfig, LandSlope, Neighborhood, Condition1, Condition2, BldgType, HouseStyle, OverallQual, OverallCond, YearBuilt, RoofStyle, RoofMatl, Exterior1st, Exterior2nd, MasVnrType, MasVnrArea, ExterQual, ExterCond, Foundation, BsmtCond, Electrical, FstFlrSF, SndFlrSF, SalePrice)

        mycursor.execute(query,data)
        connection.commit()
        return render_template('/addp.html',msg='New Property Added Successfully!')
    

@app.route('/viewpr')
def viewpr():
     query = 'select `Id`,`MSSubClass`,`MSZoning`,`LotArea`,`LotShape`,`Utilities`,`LandSlope`,`Neighborhood`,`BldgType`,`HouseStyle`,`YearBuilt`,`RoofStyle`,`Electrical`,`1stFlrSF`,`2ndFlrSF`,`SalePrice` from propertydata'
     mycursor.execute(query)
     data=mycursor.fetchall()
     return render_template('viewp.html',sqldata=data)
    
@app.route('/backadminhome')
def backadminhome():
    return render_template('admin_home.html')

@app.route('/updatep',methods=['GET','POST'])
def updatep():
    if request.method=='POST':
        pid=request.form.get('id')
        query='SELECT * FROM `propertydata` WHERE `Id`='+pid
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('/alterp.html',sqldata=data)
    return render_template('/updatep.html')


@app.route('/alterp',methods=['GET','POST'])
def alterp():
    if request.method=='POST':
        pid=request.form.get('Id')
        LotArea=request.form.get('LotArea')
        query='UPDATE `propertydata` SET `LotArea`=%s where `Id`=%s'
        data=(LotArea,pid)
        mycursor.execute(query,data)
        connection.commit()
        return render_template('alterp.html',msg="Property Data Updated Successfully!")

@app.route('/searchp')
def searchp():
    return render_template('searchp.html')

@app.route('/searchresult',methods=['GET','POST'])
def searchresult():
    if request.method == 'POST':
        pid=request.form.get('id')
        query='SELECT `Id`, `MSSubClass`, `MSZoning`, `LotArea`, `Street`, `LotShape`, `LandContour`, `Utilities`, `LotConfig`, `LandSlope`, `Neighborhood`, `Condition1`, `Condition2`, `BldgType`, `HouseStyle`, `OverallQual`, `OverallCond`, `YearBuilt`, `RoofStyle`, `RoofMatl`, `Exterior1st`, `Exterior2nd`, `MasVnrType`, `MasVnrArea`, `ExterQual`, `ExterCond`, `Foundation`, `BsmtCond`, `Electrical`, `1stFlrSF`, `2ndFlrSF`, `SalePrice` FROM `propertydata` WHERE `Id`='+pid
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('/searchresult.html',sqldata=data)


@app.route('/removepr')
def removepr():
    return render_template('/removep.html')

@app.route('/removeresult',methods=['GET','POST'])
def removeresult():
    if request.method == 'POST':
        pid=request.form.get('id')
        query='DELETE FROM `propertydata` WHERE `Id`='+pid
        mycursor.execute(query)
        connection.commit()
        return render_template('/removep.html',msg="Property with ID "+pid+" deleted successfully.")


@app.route('/searchpuser')
def searchpuser():
    return render_template('/searchpuser.html')

@app.route('/backuserhome')
def backuserhome():
    return render_template('/home.html')

@app.route('/usersearch',methods=['GET','POST'])
def usersearch():
    if request.method=='POST':
        LotArea=request.form.get('LotArea')
        query='SELECT `Id`, `MSSubClass`, `MSZoning`, `LotArea`, `Street`, `LotShape`, `LandContour`, `Utilities`, `LotConfig`, `LandSlope`, `Neighborhood`, `Condition1`, `Condition2`, `BldgType`, `HouseStyle`, `OverallQual`, `OverallCond`, `YearBuilt`, `RoofStyle`, `RoofMatl`, `Exterior1st`, `Exterior2nd`, `MasVnrType`, `MasVnrArea`, `ExterQual`, `ExterCond`, `Foundation`, `BsmtCond`, `Electrical`, `1stFlrSF`, `2ndFlrSF`, `SalePrice` FROM `propertydata` WHERE `LotArea`<='+LotArea
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('/searchresultuser.html',sqldata=data)
             
       

@app.route('/sellp',methods=['GET','POST'])
def sellp():
    if request.method=='POST':
       
        MSSubClas=request.form['MSSubClass']
        MSZoning=request.form['MSZoning']
        Street=request.form['Street']
        LotArea=request.form.get('LotArea')
        LotShape=request.form['LotShape']
        LandContour=request.form['LandContour']
        Utilities=request.form['Utilities']
        LotConfig=request.form['LotConfig']
        LandSlope=request.form['LandSlope']
        Neighborhood=request.form['Neighborhood']
        Condition1=request.form['Condition1']
        Condition2=request.form['Condition2']
        BldgType=request.form['BldgType']
        HouseStyle=request.form['HouseStyle']
        OverallQual=request.form['OverallQual']
        OverallCond=request.form['OverallCond']
        YearBuilt=request.form.get('YearBuilt')
        RoofStyle=request.form['RoofStyle']
        RoofMatl=request.form['RoofMatl']
        Exterior1st=request.form['Exterior1st']
        Exterior2nd=request.form['Exterior2nd']
        MasVnrType=request.form['MasVnrType']
        MasVnrArea=request.form.get('MasVnrArea')
        ExterQual=request.form['ExterQual']
        ExterCond=request.form['ExterCond']
        
        Foundation=request.form['Foundation']
        BsmtCond=request.form['BsmtCond']
        Electrical=request.form['Electrical']
        FstFlrSF=request.form.get('1stFlrSF')
        SndFlrSF=request.form.get('2ndFlrSF')
        SalePrice=request.form.get('SalePrice')

        query = 'INSERT INTO `propertydata`(`MSSubClass`, `MSZoning`, `LotArea`, `Street`, `LotShape`, `LandContour`, `Utilities`, `LotConfig`, `LandSlope`, `Neighborhood`, `Condition1`, `Condition2`, `BldgType`, `HouseStyle`, `OverallQual`, `OverallCond`, `YearBuilt`, `RoofStyle`, `RoofMatl`, `Exterior1st`, `Exterior2nd`, `MasVnrType`, `MasVnrArea`, `ExterQual`, `ExterCond`, `Foundation`,`BsmtCond`, `Electrical`, `1stFlrSF`, `2ndFlrSF`, `SalePrice`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data=(MSSubClas,MSZoning, LotArea, Street, LotShape, LandContour, Utilities, LotConfig, LandSlope, Neighborhood, Condition1, Condition2, BldgType, HouseStyle, OverallQual, OverallCond, YearBuilt, RoofStyle, RoofMatl, Exterior1st, Exterior2nd, MasVnrType, MasVnrArea, ExterQual, ExterCond, Foundation, BsmtCond, Electrical, FstFlrSF, SndFlrSF, SalePrice)

        mycursor.execute(query,data)
        connection.commit()
        return render_template('/sellp.html',msg='Your Property Posted for Sale Successfully!')
    
@app.route('/sell')
def sell():
    return render_template('/sellp.html')

@app.route('/buy')
def buy():
        query = 'select `Id`,`MSSubClass`,`MSZoning`,`LotArea`,`LotShape`,`Utilities`,`LandSlope`,`Neighborhood`,`BldgType`,`HouseStyle`,`YearBuilt`,`RoofStyle`,`Electrical`,`1stFlrSF`,`2ndFlrSF`,`SalePrice` from `propertydata`'
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('/buy.html',sqldata=data)
   

@app.route('/buyp',methods=['GET','POST'])
def buyp():
    if request.method == 'POST':
        pid=request.form.get('id')
        query='DELETE FROM `propertydata` WHERE `Id`='+pid
        mycursor.execute(query)
        connection.commit()
        return render_template('/confirm.html',msg="Property booked successfully.")


@app.route('/logout')
def logout():
    return render_template('/index.html')

@app.route('/vdata')
def vdata():
    query='SELECT `year`, `psold` FROM `soldproperty`'
    mycursor.execute(query)
    data=mycursor.fetchall()
    yr=[]
    ps=[]
    for i in data:
        yr.append(i[0])
        ps.append(i[1])
    pl.xlabel("Year")
    pl.ylabel("Property Sold")
    
    pl.title("Sale of Houses")
    pl.bar(yr,ps)
    pl.show()
    return render_template('/admin_home.html')




if __name__=='__main__':
    app.run(debug=True,port=5100)