import React from "react";
import { Map, TileLayer, Marker, Popup } from "react-leaflet";
import "./MapBox.css";
import L from 'leaflet';
import AwesomeMarkers from 'leaflet.awesome-markers';
import {
  Box,
  Button,
  RangeInput,
  Text,
  RadioButtonGroup,
  ResponsiveContext,
} from "grommet";
import { exportComponentAsPNG } from "react-component-export-image";
import ReactLeafletSearch from "react-leaflet-search";

import dataRaw from "../../departements-france-2020-12-21.json";

const MapBox = () => {
  const [data, setData] = React.useState([]);
  const [tile, setTile] = React.useState(3);
  const [composing, setComposing] = React.useState(50);
  const [maps] = React.useState([
    {
      name: "osm",
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    },
  ]);
  const [showInfo, setShowInfo] = React.useState(false);

  const size = React.useContext(ResponsiveContext);
  const componentRef = React.useRef();

  React.useEffect(() => {
    // Coder ici l'appel à l'api de votre choix, exemple :
    // fetch(
    //   "https://opendata.paris.fr/api/records/1.0/search/?dataset=referentiel-archeologique-de-paris&q=&facet=code_postal&facet=nature_operation&facet=responsable_operation&facet=date_operation&facet=prehistoire&facet=protohistoire&facet=antiquite&facet=moyen_age&facet=temps_modernes&facet=epoque_contemporaine"
    // )
    //   .then((response) => response.json())
    //   .then((data) => setData(data.records));
  }, []);

  return (
    <>
      {size === "small" && (
        <Box
          direction="row"
          margin="small"
          gap="small"
          align="center"
          style={{ height: "40%" }}
        >
          <Box>
            <Button
              onClick={() => setShowInfo(!showInfo)}
              label="Montrer marqueurs"
              color={tile === 0 && "red"}
            ></Button>
          </Box>
        </Box>
      )}
      <Box align="center" direction="row" fill>
        {size !== "small" && (
          <Box
            margin="small"
            gap="small"
            align="center"
            style={{ width: "20%" }}
          >
            <Button
              onClick={() => setShowInfo(!showInfo)}
              label="Montrer marqueurs"
              color={tile === 0 && "red"}
            ></Button>
          </Box>
        )}

        <Box fill>
          <Map
            center={[48.847, 2.343]}
            zoom={12}
            ref={componentRef}
            zoomControl={false}
            attributionControl={false}
          >
            <TileLayer url={maps[0].url} />

            <ReactLeafletSearch
              position="topleft"
              inputPlaceholder="Custom placeholder"
              showMarker={false}
              zoom={12}
              closeResultsOnClick={true}
              openSearchOnLoad={false}
            ></ReactLeafletSearch>

            {showInfo && (
              // Coder ici l'affichage de vos marqueurs (remplacer dans les <></> qui suivent)
              dataRaw.features.map((item) => {
                let redMarker = L.AwesomeMarkers.icon({
                  icon: 'pulse-outline',
                  markerColor: 'red'
                });
                  return (item.geometry ?
                  <Marker position={ [item.geometry.coordinates[1], item.geometry.coordinates[0]] } /*icon = {redMarker}*/ >
                    <Popup>
                      <Box margin="small" overflow="scroll" height="small">
                        <Text size="small">{ item.properties["Province/State"] }</Text>
                      </Box>
                    </Popup>
                  </Marker>
                    : ''
                  )

              })
            )}

            {/* {showInfo && (
              // Coder ici l'affichage de vos marqueurs (remplacer dans les <></> qui suivent)
              dataRaw.features.map((item) => {
                switch(item.fields.synthese_eval_sanit){
                  case "Très satisfaisant":
                    let icon1 = new L.Icon({iconUrl: 'https://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|E006E3&chf=a,s,ee00FFFF',
                      iconRetinaUrl: 'https://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|E006E3&chf=a,s,ee00FFFF',
                      iconAnchor: null,
                      popupAnchor: null,
                      shadowUrl: null,
                      shadowSize: null,
                      shadowAnchor: null,
                      iconSize: new L.Point(30, 30)})
                      return (item.geometry ?
                        <Marker position={ [item.geometry.coordinates[1], item.geometry.coordinates[0]] } icon={ icon1 }>
                          <Popup>
                            <Box margin="small" overflow="scroll" height="small">
                      <Text size="small">{item.fields.app_libelle_etablissement}</Text>
                      <Text size="small">{item.fields.synthese_eval_sanit}</Text>
                            </Box>
                          </Popup>
                        </Marker>
                        : ''
                      )
                    break;
                  case "A améliorer":
                    let icon2 = new L.Icon({iconUrl: require('./symbole_rouge.jpg'),
                      iconRetinaUrl: require('./symbole_rouge.jpg'),
                      iconAnchor: null,
                      popupAnchor: null,
                      shadowUrl: null,
                      shadowSize: null,
                      shadowAnchor: null,
                      iconSize: new L.Point(30, 30)})
                      return (item.geometry ?
                        <Marker position={ [item.geometry.coordinates[1], item.geometry.coordinates[0]] } icon={ icon2 }>
                          <Popup>
                            <Box margin="small" overflow="scroll" height="small">
                      <Text size="small">{item.fields.app_libelle_etablissement}</Text>
                      <Text size="small">{item.fields.synthese_eval_sanit}</Text>
                            </Box>
                          </Popup>
                        </Marker>
                        : ''
                      )
                    break;
                  case "Satisfaisant":
                    let icon3 = new L.Icon({iconUrl: require('./symbole_vert.png'),
                      iconRetinaUrl: require('./symbole_vert.png'),
                      iconAnchor: null,
                      popupAnchor: null,
                      shadowUrl: null,
                      shadowSize: null,
                      shadowAnchor: null,
                      iconSize: new L.Point(30, 30)})
                      return (item.geometry ?
                        <Marker position={ [item.geometry.coordinates[1], item.geometry.coordinates[0]] } icon={ icon3 }>
                          <Popup>
                            <Box margin="small" overflow="scroll" height="small">
                      <Text size="small">{item.fields.app_libelle_etablissement}</Text>
                      <Text size="small">{item.fields.synthese_eval_sanit}</Text>
                            </Box>
                          </Popup>
                        </Marker>
                        : ''
                      )
                    break;
                  case "A corriger de manière urgente":
                    let icon4 = new L.Icon({iconUrl: require('./triforce.jpg'),
                      iconRetinaUrl: require('./triforce.jpg'),
                      iconAnchor: null,
                      popupAnchor: null,
                      shadowUrl: null,
                      shadowSize: null,
                      shadowAnchor: null,
                      iconSize: new L.Point(30, 30)})
                      return (item.geometry ?
                        <Marker position={ [item.geometry.coordinates[1], item.geometry.coordinates[0]] } icon={ icon4 }>
                          <Popup>
                            <Box margin="small" overflow="scroll" height="small">
                      <Text size="small">{item.fields.app_libelle_etablissement}</Text>
                      <Text size="small">{item.fields.synthese_eval_sanit}</Text>
                            </Box>
                          </Popup>
                        </Marker>
                        : ''
                      )
                    break;
                  default:
                    let icon = new L.Icon({iconUrl: require('./triforce.svg'),
                      iconRetinaUrl: require('./triforce.svg'),
                      iconAnchor: null,
                      popupAnchor: null,
                      shadowUrl: null,
                      shadowSize: null,
                      shadowAnchor: null,
                      iconSize: new L.Point(30, 30)})
                      return (item.geometry ?
                        <Marker position={ [item.geometry.coordinates[1], item.geometry.coordinates[0]] } icon={ icon }>
                          <Popup>
                            <Box margin="small" overflow="scroll" height="small">
                      <Text size="small">{item.fields.app_libelle_etablissement}</Text>
                      <Text size="small">{item.fields.synthese_eval_sanit}</Text>
                            </Box>
                          </Popup>
                        </Marker>
                        : ''
                      )
                    break;
                }
                })

              // remplacer (<></>) par votre code
              //<></>
            )} */}

          </Map>
        </Box>
      </Box>
    </>
  );
};

export default MapBox;
