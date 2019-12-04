"""

"""
import sqlite3
from os import remove


class DatabaseManagement(object):
	"""
	This API Is Designed To Be Used As Database Manager For Hydrogen Password Manager Program.
	It Will Work As Importable Module.
	"""
	IsClose = False
	def __init__(self,databasefile):
		self.databasefile=databasefile
		self.connection=sqlite3.connect(self.databasefile)
		self.cursor = self.connection.cursor()
		#print("connection established to existing / new database.")

	def DeleteDatabase(self):
		#!this will remove whole database, [ VERY DANGEROUS ]
		sql_delq = """DELETE FROM CatagoryDetails"""
		self.cursor.execute(sql_delq)
		self.connection.commit()
		print("Whole Table Cleared.")
	"""
		self.connection.close()
		remove(self.databasefile)
		try:
			remove(self.databasefile)
			print("database removed successfully")
		except:
			print("failed to remove database ")
		"""

	def CreateTable(self):
		try:
			#!trying to create table if not exists already.
			sql_ct = """CREATE TABLE CatagoryDetails
						(ID INTEGER PRIMARY KEY,
						WORD TEXT NOT NULL UNIQUE,
						SYNONYMS TEXT NOT NULL,
						MEANING TEXT NOT NULL);"""
			self.cursor.execute(sql_ct)
			self.connection.commit()
		except sqlite3.Error as msg:
			#!no need to create just read it, table already there.
			#print(msg)
			pass

	def InsertNewDetails(self,id,accounttype,userID,passCode):
		sql_InsD = """
		INSERT INTO CatagoryDetails
		('ID','WORD','SYNONYMS','MEANING') VALUES
		('{}','{}','{}','{}')
		""".format(id,accounttype,userID,passCode)
		try:
			self.cursor.execute(sql_InsD)
			self.connection.commit()
			print("data inserted")
		except sqlite3.OperationalError as msg:
			print("INSERT Error: ",msg)
		#except:
		#	print("failed to inseet data for id : %s"%id)
		#pass
	def DeleteWholeRow(self,targetID):
		#!this method will delete whole row of data based on ID ie.primary key
		sql_dq = """DELETE FROM CatagoryDetails where ID = {}""".format(targetID)
		try:
			self.cursor.execute(sql_dq)
			self.connection.commit()
			print("Row %s removed successfully."%targetID)
			pass
		except sqlite3.OperationalError as msg:
			print(msg)
	def UpdateCredentials(self,id,updateopt,newdata):
		#!this method will allow program to manipulate details.
		#!it will take 3 things as arguments ie. unique ID, what to update in row and new data to update.
		if updateopt == "USERNAME":
			sql_ur = '''UPDATE CatagoryDetails set WORD = '{}' where ID = {};'''.format(newdata,id)
		elif updateopt == "PASSWORD":
			sql_ur = '''UPDATE CatagoryDetails set SYNONYMS = '{}' where ID = {};'''.format(newdata,id)
		elif updateopt == "ACCOUNTTYPE":
			sql_ur = '''UPDATE CatagoryDetails set MEANING = '{}' where ID = {};'''.format(newdata,id)
		else:
			pass

		self.cursor.execute(sql_ur)
		self.connection.commit()


		print("%s at ID %s updated successfully"%(updateopt,id))

	def FetchData(self):
		sql_rd = """SELECT * from CatagoryDetails"""
		self.cursor.execute(sql_rd)
		all_records = self.cursor.fetchall()
		return all_records

	def CloseConnections(self):
		if self.connection:
			self.connection.close()
		print("connection closed.")
		DatabaseManagement.IsClose = True

#x = DatabaseManagement("f4retgsd.db")
#x.CreateTable()
#x.InsertNewDetails(1,"Facebook","tanmay","xxeminemxx")
#x.InsertNewDetails(2,"rahul","xxeminemxx","asdasrae3w")
#x.InsertNewDetails("3","rohan","xxeminemxx")
#x.DeleteWholeRow(3)
#print(x.FetchData())
#x.UpdateCredentials(1,"USERNAME","Hanmay")