#!/bin/bash
rsync -avPog --chown=www-data:www-data ./build/SDP-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data ./build/PRD-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data ./build/SDD-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;