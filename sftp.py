import paramiko

# SFTP接続設定
sftp_config = {
    'host' : '153.126.189.240',
    'port' : '22',
    'user' : 'redmine_user',
	'key'  : '/home/yuta/.ssh/redmine.pem'
} 

#SSH接続の準備
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(sftp_config['host'], 
               port=sftp_config['port'],
               username=sftp_config['user'],
               key_filename=sftp_config['key'])

# SFTPセッション開始
sftp_connection = client.open_sftp() 

CONNECT_PATH = '/home/redmine_user/harada/' 
f='sample'
# attr=sftp_connection.put(f, CONNECT_PATH + f)
# print(attr)

# dir=sftp_connection.listdir(CONNECT_PATH)
# for i in dir:
# 	print(i	)

attr = sftp_connection.lstat(CONNECT_PATH + f)
print(attr)

entries  = sftp_connection.listdir(CONNECT_PATH)
print(entries)

sftp_connection.close()

client.close()