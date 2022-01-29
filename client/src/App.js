import {useState, useEffect} from 'react'

function App() {
  const [state, setState] = useState({
    message: "",
  })

  const base_url = 'https://andrewrobles.pythonanywhere.com'

  useEffect(() => {
    fetch(base_url + '/helloworld/')
    .then(response => response.json())
    .then(data => saveMessage(data.message))
    .catch( err => {
        saveMessage('Client could not fetch from server')
    })
  }, [])

  const saveMessage = (message) => {
      setState({
        message: message,
      })
  }

  return (
    <h1 className="text-3xl font-bold underline">
      {state.message}
    </h1>
  );
}

export default App;
