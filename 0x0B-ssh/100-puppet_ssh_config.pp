#!/usr/bin/env bash
# making changes  using Puppet

file_line { 'Turn off passwd auth':
 ensure => present,
 path   => '/etc/ssh/ssh_config',
 line   => 'PasswordAuthentication no',
 match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
 path  => '/etc/ssh/ssh_config',
 line  => 'IdentityFile ~/.ssh/school',
 match => '^#?IdentityFile',
}
