import buildingImg from '../assets/react.svg';
import './Landing.css';

const Landing = () => (
  <main className="landing-main">
    <div className="landing-content">
      <h1>Welcome to PropBiz</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque euismod, nisi eu consectetur consectetur, nisl nisi consectetur nisi, euismod euismod nisi nisi euismod.</p>
    </div>
    <div className="landing-image">
      <img src={buildingImg} alt="Buildings" />
    </div>
  </main>
);

export default Landing; 