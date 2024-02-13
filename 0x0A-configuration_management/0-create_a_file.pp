#creates a file in /tmp

$root_dir='/tmp/school'

file { $root_dir:
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
  content => 'I love Puppet',
}
