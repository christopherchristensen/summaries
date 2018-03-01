## LAMP

### Installing LAMP Web Server
> Easy to follow tutorial here: <br>
> https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html

### Useful Server Commands

#### Apache

**Start** Apache Server: <br>
`sudo service httpd start`

**Status** Apache Server: <br>
`sudo service httpd status`

**List documents** in Apache document root: <br>
`ls -l /var/www`

**Restart** Apache: <br>
`sudo service httpd restart`

#### MySQL

**Start** MySQL Server: <br>
`sudo service mysqld start`

**Start** MySQL Server at **every boot**: <br>
`sudo chkconfig mysqld on`

**Status** MySQL Server: <br>
`sudo service mysqld status`

**Stop** MySQL Server: <br>
`sudo service mysqld stop`



