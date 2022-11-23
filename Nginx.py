user  byhy;          
worker_processes  2; 

events {
   
    worker_connections  1024; 
}


worker_rlimit_nofile 2000;

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;

    keepalive_timeout  30;

    gzip  on;
 
    upstream apiserver  {

        # maintain a maximum of 20 idle connections to each upstream server
        keepalive 20;

        server 127.0.0.1:8000; 
    }
   
