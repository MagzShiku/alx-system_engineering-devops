# make nginx open more files to avoid failed requests

exec { 'set limit to 2000 and reboot nginx':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx && /usr/sbin/service nginx restart"
}
