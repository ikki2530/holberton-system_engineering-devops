# 0x09. Web infrastructure design

# Description
This project shows how are design basic web infrastructures including databases, web servers, app servers, load balancer, firewalls, ssl certificate.

# Learning objectives
- You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
- You must be able to explain what each component is doing
- You must be able to explain system redundancy
- Know all the mentioned acronyms: LAMP, SPOF, QPS


# Files
## [0-simple_web_stack](./0-simple_web_stack)
You must add:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8


## [1-distributed_web_infrastructure](./1-distributed_web_infrastructure)
You must add:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)


## [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure)
You must add:
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)


## Author
Diego Gómez


