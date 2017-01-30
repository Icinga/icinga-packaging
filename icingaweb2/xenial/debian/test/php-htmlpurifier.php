<?php

require_once 'HTMLPurifier/Bootstrap.php';
require_once 'HTMLPurifier.php';
require_once 'HTMLPurifier.autoload.php';

$config = HTMLPurifier_Config::createDefault();
$config->set('Core.EscapeNonASCIICharacters', true);
$config->set('HTML.Allowed', 'p,br,b,a[href],i,table,tr,td[colspan],div[class]');

if (assert(get_class($config) == 'HTMLPurifier_Config') === true) {
    echo "HTMLPurifier loaded successfully.\n";
}
else {
    exit(1);
}
