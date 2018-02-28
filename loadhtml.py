
import ftplib
 
server = 'ftp.w02.wh-2.com'
username = 'zoomfrog_raspberry'
password = 'Raspberry'
ftp_connection = ftplib.FTP(server, username, password)
remote_path = ""
ftp_connection.cwd(remote_path)
fh = open("default.html", 'rb')
ftp_connection.storbinary('STOR default.html', fh)
fh.close()
