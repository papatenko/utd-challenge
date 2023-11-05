import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Header />
    </div>
  );
}

function Header() {
  return (
    <header>
      <h1 className="title">Header</h1>
      <div className="hyperlinks">
        <h2>about us</h2>
        <h2>search</h2>
      </div>
    </header>
  );
}

export default App;
