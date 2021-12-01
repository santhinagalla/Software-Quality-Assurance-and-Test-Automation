# Steps to run Code -  
1. Make sure the mysql server up and running  
2. And start python3 server using below command -  
                    python3 -m http.server 8000 --bind 127.0.0.1 --cgi  
3. Save and change the mode of the File using command - chmod 755 dos.sh  
4. Go to https://www.google.com/recaptcha/admin/create to create a reCAPTCHA to prevent the attack.  
5. Copy the client-side key and use in index.html.  
6. Copy the Server-side key and use in songlist.py.
7. Launch the browser and Open http://localhost:8000/ to see Online Jukebox form.
