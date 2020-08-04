# Task 4, ssh project
file_line { 'namefile':
    ensure => present,
    line   => 'Hello world',
}