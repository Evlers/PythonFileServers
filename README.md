## File servers
File servers base python3

## Install
```
sudo apt install python3
sudo apt install python3-pip
sudo pip install flask gevent
```

## Running service
```
# Copy service file to systemd folder, add to the system service
sudo cp file_servers.service /usr/lib/systemd/system/
sudo systemctl daemon-reload

# Start the service and enable startup
sudo systemctl start file_servers
sudo systemctl enable file_servers
```

## Test
```
# Test upload file
http://192.168.x.x:6443/upload

# Test download file
http://192.168.x.x:6443/file/xxxx
```
