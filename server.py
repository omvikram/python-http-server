import SocketServer
import SimpleHTTPServer
import re
#import mysql.connector

PORT = 8088 ##You can choose your port which is available to you

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if None != re.search('/api/square/*', self.path):
            num = float(self.path.split('/')[-1])
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(str(num*num)) #call sample function here
            return
        if None != re.search('/api/mult/*', self.path):
            num1 = float(self.path.split('/')[-1])
            num2 = float(self.path.split('/')[-2])
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(str(num1*num2)) #call sample function here
            return
        # if None != re.search('/api/mysql/*', self.path):
        #     ms = ""
        #     try:
        #         mydb = mysql.connector.connect(host="localhost",user="root",password="",database="sys")
        #         msg = "MySQL Connection is Successful"
        #     except:
        #         msg = "MySQL Connection is UnSuccessful"
        #      #This URL will trigger a db connection and returns back the localhost db connection to the browser
        #     self.send_response(200)
        #     self.send_header('Content-type','text/html')
        #     self.end_headers()
        #     self.wfile.write(msg) 
        else:
            #serve files, and directory listings by following self.path from
            #current working directory
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.ThreadingTCPServer(("127.0.01", PORT), CustomHandler)
print("serving at port", PORT)
httpd.serve_forever()