# Solve the Apache Error 500
exec {'fix-wordp ress':
    command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
    path    => '/usr/bin',
}
