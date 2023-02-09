import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Libran@0203",
 database="emergency_supplies"
)
c = mydb.cursor()

def add_data(dealer_id, dealer_name, dealer_address, dealer_item, dealer_transport):
    c.execute('INSERT INTO VOLUNTEER VALUES (%s,%s,%s,%s,%s)',(dealer_id, dealer_name, dealer_address, dealer_item, dealer_transport))
    mydb.commit()

def view_user_data():
 c.execute('SELECT * FROM USER')
 data = c.fetchall()
 return data

def view_vol_data():
    c.execute('SELECT * FROM VOLUNTEER')
    data = c.fetchall()
    return data

def view_ware_data():
    c.execute('SELECT * FROM WAREHOUSE')
    data = c.fetchall()
    return data

def edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin,new_dealer_street, dealer_id):
    c.execute("UPDATE VOLUNTEER SET V_ID=%s, NAME=%s, ADDRESS=%s, ITEM=%s,TRANSPORT=%s WHERE V_ID=%s ", (new_dealer_id, new_dealer_name, new_dealer_city,new_dealer_pin, new_dealer_street, dealer_id))
    mydb.commit()
    data = c.fetchall()
    return data
    
def delete_data(dealer_name):
 c.execute('DELETE FROM VOLUNTEER WHERE V_ID="{}"'.format(dealer_name))
 mydb.commit()

def display_vol(dealer_id):
    c.execute('SELECT * FROM WAREHOUSE WHERE V_ID = %s',(dealer_id,))
    data = c.fetchall()
    return data