dropdb timezone
createdb timezone -O homeland
createlang plpgsql timezone
psql -d timezone -f /usr/share/postgresql/8.4/contrib/postgis.sql
psql -d timezone -d timezone -f /usr/share/postgresql/8.4/contrib/spatial_ref_sys.sql 
psql timezone -c 'alter table geometry_columns owner to homeland'
psql timezone -c 'alter table spatial_ref_sys owner to homeland'
#psql timezone -e -f data/srid.sql
python manage.py syncdb
