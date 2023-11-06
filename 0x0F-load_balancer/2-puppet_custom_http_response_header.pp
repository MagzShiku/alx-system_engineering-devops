#!/usr/bin/python3
"""
using puppet to install ngix and add hearder
"""

class custom_http_response_header {
 package { 'nginx':
 ensure => 'installed',
 }

 file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
   http {
    server {
     listen 80 default_server;
     listen [::]:80 default_server;
     server_name _;
     root /var/www/html;

     location / {
      add_header X-Served-By $hostname;
     }
    }
   }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
 }
  
 file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
 }
 
 service { 'nginx':
  ensure => 'running',
  enable => true,
 }
}

include custom_http_response_header
