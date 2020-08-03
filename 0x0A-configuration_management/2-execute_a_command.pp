# Task2: kill the process
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin',
}