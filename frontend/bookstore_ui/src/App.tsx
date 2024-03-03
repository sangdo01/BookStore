import React from 'react';
import './App.css';

function App() {
  return (
    <div>
      react app {process.env.NODE_ENV}
      react app {process.env.REACT_APP_API_URL}
    </div>
  );
}

export default App;
