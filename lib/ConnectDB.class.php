<?php
class ConnectDB extends SQLite3
{
    function __construct()
    {
        $this->open('/home/server/Backup/tautulliLN.db');
    }
}

?>
