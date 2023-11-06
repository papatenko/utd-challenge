import logo from './logo.svg';
import './App.css';
import React from 'react';
import Navbar from './components/Navbar';
import {
    BrowserRouter as Router,
    Routes,
    Route,
    BrowserRouter,
} from 'react-router-dom';

import Home from './pages';
import About from './pages/about';
import HouseRoyale from './pages/HouseRoyale';

// function App() {
//   return (
//     <div className="App">
//       <Header />
//     </div>
//   );
// }

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/HomeRoyale" element={<HouseRoyale />} />
            </Routes>
        </Router>
    );
}

// function Header() {
//   return (
//     <header>
//       <h1 className="title">Header</h1>
//       <div className="hyperlinks">
//         <h2>about us</h2>
//         <h2>search</h2>
//       </div>
//     </header>
//   );
// }

<BrowserRouter></BrowserRouter>;

export default App;
