user  byhy;          
worker_processes  2; 

events {
   
    worker_connections  4096; 
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

        server 127.0.0.1:80; 
    }
   
    server {
     
        server_name  www.byhy.com;  

，        
        root /home/byhy/bysms_frontend/z_dist;
        
       
        location /api/      {
            proxy_pass         http://apiserver;
            proxy_set_header   Host $host;
        }
    }

}
