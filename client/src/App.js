import Globe from 'worldwind-react-globe'

function App() {
  const layers = [
    {layer: 'blue-marble', options: {category: 'base', enabled: true}},
    {layer: 'blue-marble-landsat', options: {category: 'base', enabled: false}},
    {layer: 'bing-aerial', options: {category: 'base', enabled: false}},
    {layer: 'bing-aerial-labels', options: {category: 'base', enabled: false}},
    {layer: 'eox-sentinal2', options: {category: 'base', enabled: false}},
    {layer: 'eox-sentinal2-labels', options: {category: 'base', enabled: true}},
    {layer: 'eox-openstreetmap', options: {category: 'overlay', enabled: false, opacity: 0.8}},
    {layer: 'bing-roads', options: {category: 'overlay', enabled: false, opacity: 0.8}},
    {layer: 'renderables', options: {category: 'data', enabled: true, displayName: 'Markers'}},
    {layer: 'compass', options: {category: 'setting', enabled: false}},
    {layer: 'coordinates', options: {category: 'setting', enabled: true}},
    {layer: 'view-controls', options: {category: 'setting', enabled: true}},
    {layer: 'stars', options: {category: 'setting', enabled: false}},
    {layer: 'atmosphere-day-night', options: {category: 'setting', enabled: false}}
  ]

  return (
    <div>
      <Globe layers={layers}/>
    </div>
  );
}

export default App;
