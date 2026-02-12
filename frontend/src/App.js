import { useEffect } from "react";

function App() {
  useEffect(() => {
    fetch("http://localhost:8000/")
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.error(err));
  }, []);

  return <h1>Check console for API result</h1>;
}

export default App;
