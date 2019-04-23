#!/bin/bash
rsync -avPog --chown=www-data:www-data -e ssh ./build/SDP-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data -e ssh ./build/PRD-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;
rsync -avPog --chown=www-data:www-data -e ssh ./build/SDD-html deploy@ali.cnworkshop.xyz:/var/www/shattuckite-doc;