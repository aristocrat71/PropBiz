import './App.css';
import Landing from './components/Landing';
import LandingNavbar from './components/LandingNavbar';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <LandingNavbar />
      <Landing />
      <Footer />
    </div>
  );
}

export default App;
