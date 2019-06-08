#!/bin/bash
rsync -avPog --chown=www-data:www-data -e ssh ./build/SDP-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data -e ssh ./build/SRS-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data -e ssh ./build/SDD-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data -e ssh ./build/STR-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;