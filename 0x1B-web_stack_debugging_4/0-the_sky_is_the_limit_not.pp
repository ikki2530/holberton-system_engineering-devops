# Solve the Apache Error 500
exec {'fix--for-nginx':
    command => "sed -i 's/15/1000/g' /etc/default/nginx",
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec {'arestart-nginx':
    command => 'service nginx restart',
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
