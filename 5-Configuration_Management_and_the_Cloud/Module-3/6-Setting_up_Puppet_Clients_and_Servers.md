# Setting up Puppet Clients and Servers

## About this code

This command configures Puppet to automatically sign the certificate requests of added nodes.

```puppet
sudo puppet config --section master set autosign true
```

---

## About this code
The command ssh webserver allows you to ssh into a machine called webserver. The sudo apt install puppet installs the Puppet agent onto webserver with the Puppet package. Then, the command sudo puppet config set server ubuntu.example.com configures Puppet to talk to the server on ubuntu.example.com.

```puppet
ssh webserver
sudo apt install puppet
sudo puppet config set server ubuntu.example.com
```

---

## About this code

This code tests the connection between the Puppet agent on the machine and the Puppet master. The -v command indicates that the output should be verbose, and the --test command indicates that this is a test run. 

```puppet
sudo puppet agent -v --test
```

---

## About this code
View and create the site.pp manifest file by entering editing mode with the vim command. First, to install Apache on the webserver nodes, define the webserver node with the node webserver command, and then include the Apache class without any parameters with class{‘apache’}. Second, define the default node definition with the code node default{}. We won’t add any classes yet. 

```puppet
vim /etc/puppet/code/environments/production/manifests/site.pp

node webserver {
  class { 'apache': }
}

node default {}
```

---

## About this code
This code uses the systemctl command to enable the puppet service with the enable parameter so that the Puppet agent is started whenever the machine reboots. 

```puppet
sudo systemctl enable puppet
```

---

## About this code
This code starts the puppet service with the start parameter, then checks its status with the status parameter. 

```puppet
sudo systemctl start puppet
sudo systemctl status puppet
```

---

