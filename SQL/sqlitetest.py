import sqlite3
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# try:
#       c.execute("update COMPANY set salary='95000' where name=Te")
#       conn.commit()
# except sqlite3.OperationalError:
#       print("update failed")
#       conn.close()
with sqlite3.connect('test.db') as conn:
      c=conn.cursor()
      c.execute("update COMPANY set salary='95000' where name=Te")
      conn.commit()