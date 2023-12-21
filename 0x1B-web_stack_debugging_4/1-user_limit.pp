# change the OS configuration so I can log in with Holberton user and open the file without error

exec { 'setting limits':
  command => "sed -i 's/5/4000/' /etc/security/limits.conf && sed -i 's/4/2000/' /etc/security/limits.conf",
  path    => '/bin'
}
