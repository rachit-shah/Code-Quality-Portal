
# MILESTONE 4

## 1. Steps to Deploy Our Application on Digital Ocean
**Steps adopted from [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) tutorial** 

#### Creating Droplet on DigitalOcean
1. Create an account on Digital Ocean and buy an Ubuntu 18.04 droplet
2. Add the necessary SSH keys to access the droplet remotely via terminal

#### Creating Domain Name
1. Create a domain name on sites like FreeNom (e.g., codequalityportal.tk). 
2. Add ip address of the droplet to their DNS service when buying the domain name.
3. Add ns1.digitalocean.com, ns2.digitalocean.com and ns3.digitalocean.com to the nameserver on FreeNom client area.
4. Add the domain to DigitalOcean's droplet

#### Prerequisites
1. [Create a non-root user on the droplet and ssh to the droplet using that user. We create a non-root user named sammy. If you use another name, change the consecutive steps accordingly.](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)
2. [Install nginx on the droplet.](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
3. Domain name should redirect to "Welcome nginx" page after following the above steps

#### Setup Environment
1. Install python and other packages from terminal.
```
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```
2. Clone our repository and switch to branch "deploy".
3. Create a Python3 virtual env
```
sudo apt install python3-venv
python3.6 -m venv myprojectenv
source myprojectenv/bin/activate
```
4. Install all requirements.
```
cd csc510-project/CodeQualityPortal
pip install -r requirements.txt
```

#### Check if the app works on localhost
1. Open port 5000 in the firewall to let remote users access the hosted app on localhost
```
sudo ufw allow 5000
```
2. Before deploying the app check if the app works on the localhost by following these steps from the first CodeQualityPortal folder in the repo
```
cd csc510-project/CodeQualityPortal
export FLASK_APP=__init__
flask run --host=0.0.0.0
```
3. Accessing the site with the domain name/ip address and port should open the app in the browser.
```
http://your_server_ip:5000 (e.g. http://codequalityportal.tk:5000)
```
4. Close the flask run command.

#### Configuring uWSGI
1. Test if uWSGI is working to deploy our app using the following command.
```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```
2. Again accessing the site with the domain name/ip address and port should open the app in the browser.
```
http://your_server_ip:5000 (e.g. http://codequalityportal.tk:5000)
```
3. Close the command and deactivate the virtual environment
```
deactivate
```

#### Creating a systemd Unit File
1. Create a systemd unit service file which will allow Ubuntu's init system to automatically start uWSGI and serve the Flask application whenever the server boots.
```
sudo nano /etc/systemd/system/CodeQualityPortal.service
```
2. Add the following code changing user name and paths accordingly
```
[Unit]
Description=uWSGI instance to serve CodeQualityPortal
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/CodeQualityPortal
Environment="PATH=/home/sammy/myprojectenv/bin"
ExecStart=/home/sammy/myprojectenv/bin/uwsgi --ini CodeQualityPortal.ini

[Install]
WantedBy=multi-user.target
```
3. Start the uWSGI service we created and enable it so that it starts at boot
```
sudo systemctl start CodeQualityPortal
sudo systemctl enable CodeQualityPortal
```
4. Check the status and check that it returns active
```
sudo systemctl status CodeQualityPortal
```

#### Configuring Nginx to Proxy Requests
1. Create a new server block configuration file in Nginx's sites-available directory named CodeQualityPortal
```
sudo nano /etc/nginx/sites-available/CodeQualityPortal
```
2. Add the following to the file while changing domain name, user name, paths and ports as needed. 
```
server {
    listen 80;
    server_name codequalityportal.tk www.codequalityportal.tk;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/sammy/CodeQualityPortal/CodeQualityPortal.sock;
    }
}
```
3. Enable the Nginx server block configuration you've just created and link the file to the sites-enabled directory. Test for syntax errors
```
sudo ln -s /etc/nginx/sites-available/CodeQualityPortal /etc/nginx/sites-enabled
sudo nginx -t
```
4. If there are no syntax errors, restart the Nginx process to read the new configuration.
```
sudo systemctl restart nginx
```
5. Adjust firewall to open ports
```
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
6. Done! This should deploy the app. Check your domain name to see if its working. [http://codequalityportal.tk](http://codequalityportal.tk)

7. Check logs to see if there are any errors.
```
cat ~/log/CodeQualityPortal.log
```

## 2. Data Ingest/Update

**1. Ingest:** After being provided with a valid repository url, we use GithubAPI to parse through the entire repo and scrape the content of the java files. Then we parse through each java file and calculate the following metrics:
-   Number of Methods per Class
-   Class Hierarchy Level
-   Number of Comment Lines per Class
-   Lines of Code
-   Number of Collaborators for Repository
-   Cyclomatic Complexity per Class
-   Coupling between Objects

To calculate the first five metrics we have designed and implemented our own python code. While parsing through the code we utilised characters such as /, *, { and } as well as regex to aid us in calculating the metrics.

To calculate cyclomatic complexity we used [lizard](https://github.com/terryyin/lizard) and for coupling between objects we used [this project.](https://github.com/mauricioaniche/ck).

**2. Update:** Once the user enters a repository link for the first time our portal will scrape the repository every day to record the changes in data over time. In order to do this we call the functions that perform the scraping every day by using a BackgroundScheduler in python. This scheduler allows us to execute code at any custom time interval. 

We have created a tableau private server and generated visualisations in order to visualise the data ingest/update.


 
     
     
     
   
     
    

