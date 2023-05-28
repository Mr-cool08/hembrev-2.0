from mega import Mega as m
file = m.find('supergoodfile.txt')
m.download(file)
m.download_url('https://mega.nz/file/oDVF3CRQ#0x02lHkAZBlxF67UDKWSugdyWdTY2gRMFksV_JL86C4')
m.download(file, '/home/john-smith/Desktop')