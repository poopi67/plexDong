<?php
class ConnectDB extends SQLite3
{
    function __construct()
    {
        $this->open('tautulli.db');
    }
}

?>
