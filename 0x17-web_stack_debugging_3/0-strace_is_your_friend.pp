# this code is supposed to fix things, but I have no error

exec { 'fix-wordpress-php-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
