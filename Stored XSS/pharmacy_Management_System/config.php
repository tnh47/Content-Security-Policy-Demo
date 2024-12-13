<?php
header("Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; object-src 'none';");
?>
<?php

// Database Details

define( "DB_HOST", "localhost" );
define( "DB_USER", "root" );
define( "DB_PASSWORD", "" );
define( "DB_NAME", "pms" );
