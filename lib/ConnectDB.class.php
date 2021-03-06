<?php
class ConnectDB extends SQLite3
{
    function __construct()
    {
        // This is the default location of the tautulli.db file, you may need to make a copy/hardlink as the default permissions of this directory may prevent it
        // from being usable.
        $this->open('/opt/Tautulli/tautulli.db');
    }
}

?>
