# midterm-philsoil
online deployment is not yet functional for map page, but offline localhost:3000 will

in connecting the wms from geoserver, just double check the url 
  ex: 
      var add_soils = new ol.layer.Tile({
  // layers
  title: "Phil Soil",
   opacity:1,
  source: new ol.source.TileWMS({
    //your geoserver url may be different
    url: "http://localhost:8080/geoserver/ITE-18-WEBGIS/wms",
    params: {
      LAYERS: "ITE-18-WEBGIS:projected_soil",
      TILED: true,
    },
    serverType: "geoserver",
    visible: true,
  }),
});

