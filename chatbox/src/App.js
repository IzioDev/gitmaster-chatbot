import React from 'react';
import { Widget } from 'rasa-webchat';
import './App.css';

function App() {
  localStorage.clear()
  return (
    <Widget
      initPayload={"/greet"}
      socketUrl={"http://localhost:5005"}
      // socketPath={"/socket.io/"}
      // customData={{"language": "en"}} // arbitrary custom data. Stay minimal as this will be added to the socket
      title={"GitMaster Chatbot"}
      storage={"local"}
    />
  );
}

export default App;
