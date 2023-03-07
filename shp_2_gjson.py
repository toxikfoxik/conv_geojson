import geopandas

myshpfile = geopandas.read_file(r'C:\Users\mkwlodarz\desktop\conv_shp_2_geojson\True_Ortho_0953_62969.shp')
myshpfile.to_file('myJson1.geojson', driver='GeoJSON')